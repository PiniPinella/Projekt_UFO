#!/usr/bin/env python
# coding: utf-8

# Vorgehensweise für das Area 51-Special
# 
# Den Datensatz einlesen
# 
# Wir laden den UFO-Datensatz mit Pandas.
# 
# Prüfen die Spalten und Datenstruktur, um sicherzustellen, dass die relevanten Informationen enthalten sind.
# 
# Area 51-Koordinaten bestimmen
# 
# Area 51 liegt in Nevada, USA. Wir brauchen den genauen geografischen Bereich (Longitude & Latitude).
# 
# Daten filtern
# 
# Wir filtern nur Sichtungen, die innerhalb des Koordinatenbereichs von Area 51 liegen.
# 
# Analysen durchführen
# 
# Anzahl der Sichtungen berechnen.
# 
# Tageszeit der Sichtungen analysieren.
# 
# Formen der Objekte auswerten.
# 
# Trends visualisieren (z. B. Histogramm für die Tageszeiten).
# 
# Ergebnisse visualisieren
# 
# Diagramme erstellen (z. B. Barplot, Lineplot oder Scatterplot)

# In[54]:


import pandas as pd


# In[55]:


df_area51 = pd.read_csv(r"C:\Users\Admin\Desktop\Data Craft\UFO\Projekt_UFO\data\data_clean\ufo_sightings_scrubbed_clean.csv")


# In[56]:


df_area51.head()


# In[57]:


df_area51.columns


# In[58]:


df_area51.info()


# In[59]:


df_area51.isnull().sum()


# In[ ]:





# Area 51 liegt in Nevada, USA, nahe der Groom Lake Air Force Base .
# Die ungefähren Koordinaten von Area 51 sind:
# 
# Wir filtern jetzt alle Sichtungen heraus, die innerhalb dieses Bereich sind
# Geocoder für Area 51
# 

# In[60]:


# pip install geopy
# Importiere die Nominatim-Klasse aus der geopy.geocoders-Bibliothek.
# Nominatim ist ein Geocoding-Service, der Adressen in geografische Koordinaten umwandelt.

from geopy.geocoders import Nominatim

# Erstelle ein Geolokalisierungsobjekt (geolokalisierer).
# Der Parameter "user_agent" ist notwendig, da Nominatim diesen benötigt, um den Ursprung der Anfrage zu identifizieren.

geolokalisierer = Nominatim(user_agent="ufo_sightings_analysis")

# Verwende die Methode "geocode", um die Adresse "Area 51, Nevada, USA" in geografische Koordinaten (Breitengrad und Längengrad) umzuwandeln.
# Diese Methode sendet eine Anfrage an den Nominatim-Service.
standort = geolokalisierer.geocode("Area 51, Nevada, USA")

# Überprüfe, ob der Standort gefunden wurde.
if standort:
    # Falls ein Standort gefunden wurde, gib den Breitengrad (latitude) und Längengrad (longitude) aus.
    # f-Strings werden verwendet, um die Variablen direkt in den Ausgabestring einzubetten.
    print(f"Breitengrad: {standort.latitude}, Längengrad: {standort.longitude}")
else:
    # Falls kein Standort gefunden wurde, informiere den Benutzer darüber.
    print("Standort nicht gefunden.")


# In[ ]:





# In[61]:


#  Koordinaten von Area 51
area51_lat = 37.2360646
area51_lon = -115.812175


radius = 0.05#entspricht 5 kilometer

df_area51 = pd.read_csv(r"C:\Users\Admin\Desktop\Data Craft\UFO\Projekt_UFO\data\data_clean\ufo_sightings_scrubbed_clean.csv")

# Filtern der Sichtungen innerhalb des definierten Radius
#In Pandas wird der &-Operator verwendet, um mehrere Bedingungen für das Filtern eines DataFrames zu kombinieren,
#da er sicherstellt, dass beide Bedingungen gleichzeitig wahr sind, während ein Komma zu einem Fehler führen würde,
#  weil es die Bedingungen als separate Argumente interpretiert
df_area51 = df_area51[  # Verwende den richtigen DataFrame "df_area51"
    (df_area51["latitude"].astype(float) >= area51_lat - radius) & 
    (df_area51["latitude"].astype(float) <= area51_lat + radius) & 
    (df_area51["longitude"].astype(float) >= area51_lon - radius) & 
    (df_area51["longitude"].astype(float) <= area51_lon + radius)
]

# Ergebnisse anzeigen
print(f"Anzahl der Sichtungen in der Nähe von Area 51: {len(df_area51)}")
print(df_area51.head())


# In[62]:


radius10 = 0.10
df_area51 = df_area51[  # Verwende den richtigen DataFrame "df_area51"
    (df_area51["latitude"].astype(float) >= area51_lat - radius) & 
    (df_area51["latitude"].astype(float) <= area51_lat + radius) & 
    (df_area51["longitude"].astype(float) >= area51_lon - radius) & 
    (df_area51["longitude"].astype(float) <= area51_lon + radius)
]

# Ergebnisse anzeigen
print(f"Anzahl der Sichtungen in der Nähe von Area 51: {len(df_area51)}")
print(df_area51.head())


# In[63]:


radius20 = 0.20
df_area51 = df_area51[  # Verwende den richtigen DataFrame "df_area51"
    (df_area51["latitude"].astype(float) >= area51_lat - radius) & 
    (df_area51["latitude"].astype(float) <= area51_lat + radius) & 
    (df_area51["longitude"].astype(float) >= area51_lon - radius) & 
    (df_area51["longitude"].astype(float) <= area51_lon + radius)
]

# Ergebnisse anzeigen
print(f"Anzahl der Sichtungen in der Nähe von Area 51: {len(df_area51)}")
print(df_area51.head())


# In[64]:


radius30 = 30
df_area51 = df_area51[  # Verwende den richtigen DataFrame "df_area51"
    (df_area51["latitude"].astype(float) >= area51_lat - radius) & 
    (df_area51["latitude"].astype(float) <= area51_lat + radius) & 
    (df_area51["longitude"].astype(float) >= area51_lon - radius) & 
    (df_area51["longitude"].astype(float) <= area51_lon + radius)
]

# Ergebnisse anzeigen
print(f"Anzahl der Sichtungen in der Nähe von Area 51: {len(df_area51)}")
print(df_area51.head())


# Sichtungen nach Tageszeit analysieren

# In[65]:


# wandeln die 'duration_seconds' in ein timedelta-Objekt um
df_area51["duration"] = pd.to_timedelta(df_area51["duration_seconds"], unit= "s")
print(df_area51["duration"].head())


# In[66]:


df_area51["duration_hour"] = df_area51["duration"].dt.total_seconds() / 3600
print(df_area51[["duration_seconds", "duration", "duration_hour" ]].head())


# In[71]:


df_area51["time_of_day"] = df_area51["duration_hour"].apply(lambda x: "Tag" if 6 <= x < 18 else "Nacht" )
print(df_area51[["datetime", "duration_hour", "time_of_day"]].head())


# In[81]:


df_area51


# In[ ]:


# Stelle sicher, dass 'datetime' ein DateTime-Objekt ist
df_area51['datetime'] = pd.to_datetime(df_area51['datetime'], errors='ignore')

# Extrahiere die Stunde der Sichtung
df_area51['hour'] = df_area51['datetime'].dt.hour

# Weise die Tageszeit basierend auf der Sichtungsstunde zu
df_area51["time_of_day"] = df_area51["hour"].apply(lambda x: "Tag" if 6 <= x < 18 else "Nacht")

# Überprüfe das Ergebnis
print(df_area51[["datetime", "duration_seconds" ,"time_of_day"]].head())


# In[ ]:





# In[ ]:




