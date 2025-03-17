import pandas as pd
import os
import numpy as np
from geopy.geocoders import Nominatim
import seaborn as sns
import matplotlib.pyplot as plt


def load_ufo_data():
    """
    Lädt das UFO-Dataset, indem der Speicherort des Skripts ermittelt wird.
    Der Pfad zur CSV-Datei wird relativ zum Verzeichnis des Skripts angegeben.
    """
    path_to_this_dir = os.path.abspath(os.path.dirname(__file__))
    ROOT_DIR = os.path.join(path_to_this_dir, "..")
    path_to_data_clean_read = os.path.join(ROOT_DIR, "data", "data_clean", "ufo_sightings_scrubbed_clean.csv")

    df = pd.read_csv(path_to_data_clean_read)
    return df


# Lade die UFO-Daten
df = load_ufo_data()


# Geokoordinaten für Area 51 ermitteln
geolokalisierer = Nominatim(user_agent="ufo_sightings_analysis")

try:
    standort = geolokalisierer.geocode("Area 51, Nevada, USA")
    if standort:
        area51_lat = standort.latitude
        area51_lon = standort.longitude
        print(f"Breitengrad: {area51_lat}, Längengrad: {area51_lon}")
    else:
        raise ValueError("Standort nicht gefunden.")
except Exception as e:
    print(f"Fehler bei der Geokodierung von Area 51: {e}")
    area51_lat, area51_lon = None, None


def haversine(lat1, lon1, lat2, lon2):
    """
    Berechnet die Entfernung zwischen zwei Punkten auf der Erde mit der Haversine-Formel.
    Die Ausgabe ist in Kilometern.
    """
    R = 6371  # Erdradius in km
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)

    a = np.sin(delta_phi / 2.0)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2.0)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c  # Entfernung in km


def filter_sightings_by_radius(df, lat, lon, radius_km):
    """
    Filtert UFO-Sichtungen innerhalb eines bestimmten Radius um eine gegebene Koordinate.
    """
    # Falls die Koordinaten von Area 51 nicht gefunden wurden, stoppen wir hier
    if lat is None or lon is None:
        print("Area 51-Koordinaten sind nicht verfügbar. Keine Sichtungen gefiltert.")
        return pd.DataFrame()

    df["distance_km"] = df.apply(lambda row: haversine(lat, lon, row["latitude"], row["longitude"]), axis=1)
    filtered_df = df[df["distance_km"] <= radius_km]

    print(f"Anzahl der Sichtungen im Umkreis von {radius_km} km um ({lat}, {lon}): {len(filtered_df)}")
    return filtered_df


# Radius von 30 km um Area 51 festlegen
radius_km = 30  

# UFO-Sichtungen um Area 51 filtern
df_area51 = filter_sightings_by_radius(df, area51_lat, area51_lon, radius_km)

# Sicherstellen, dass es gefilterte Daten gibt, bevor fortgefahren wird
if df_area51.empty:
    print("Keine UFO-Sichtungen in diesem Bereich gefunden.")
else:
    # Erste Zeilen der gefilterten Daten anzeigen
    print(df_area51[["datetime", "shape", "latitude", "longitude", "distance_km"]].head())

    # Dauer in Stunden umrechnen
    df_area51["duration_hour"] = df_area51["duration_seconds"] / 3600
    print(df_area51[["duration_seconds", "duration_hour"]].head())

    # Stelle sicher, dass datetime ein DateTime-Objekt ist
    df_area51["datetime"] = pd.to_datetime(df_area51["datetime"], errors="coerce")

    # Extrahiere die Stunde der Sichtung
    df_area51["hour"] = df_area51["datetime"].dt.hour

    # Weise die Tageszeit basierend auf der Sichtungsstunde zu
    df_area51["time_of_day"] = df_area51["hour"].apply(lambda x: "Tag" if 6 <= x < 18 else "Nacht")

    # Überprüfe das Ergebnis
    print(df_area51[["datetime", "duration_seconds", "time_of_day"]].head())

    # Zähle die Sichtungen für "Tag" und "Nacht"
    time_counts = df_area51["time_of_day"].value_counts()

    plt.figure(figsize=(6, 4))

    # Manuelle Reihenfolge: Erst "Tag", dann "Nacht"
    time_counts = time_counts.reindex(["Tag", "Nacht"])

    # Balkendiagramm 
    time_counts.plot(kind="bar", color=["orange", "darkblue"])

    # Achsenbeschriftungen und Titel 
    plt.xlabel("Tageszeit")
    plt.ylabel("Anzahl der Sichtungen")
    plt.title("UFO-Sichtungen nach Tageszeit in Area 51")

    # X-Achsen-Beschriftung waagerecht ausrichten
    plt.xticks(rotation=0)

    plt.savefig("UFO_Tageszeit.png")
    plt.show()

    # Wir holen uns aus datetime nur das Jahr
    df_area51["year"] = df_area51["datetime"].dt.year

    # Wir zählen, wie oft jedes Jahr eine Sichtung registriert wurde
    df_trend = df_area51.groupby("year").size().reset_index(name="count")

    plt.figure(figsize=(12, 6))
    plt.plot(df_trend["year"], df_trend["count"], marker="o", linestyle="-", color="blue")

    plt.xlabel("Jahr")
    plt.ylabel("Anzahl der Sichtungen")
    plt.title("UFO-Sichtungen in Area 51 über die Jahre")
    plt.grid(True)

    plt.savefig("UFO_Sichtungen_in_Area_51_über_die_Jahre.png")
    plt.show()

    # Hole das Jahr und die Stunde aus der datetime-Spalte
    df_area51["year"] = df_area51["datetime"].dt.year  # Holt das Jahr der Sichtung
    df_area51["hour"] = df_area51["datetime"].dt.hour  # Holt die Stunde der Sichtung (0-23)

    # Pivot-Tabelle erstellen, um die Sichtungshäufigkeit nach Jahr und Stunde darzustellen
    heatmap_data = df_area51.pivot_table(
        index="hour",  # Stunden als Zeilen (0 bis 23)
        columns="year",  # Jahre als Spalten
        aggfunc="size",  # Zählt die Anzahl der Sichtungen
        fill_value=0  # Falls keine Sichtungen existieren, trage eine 0 ein
    )

    # Heatmap
    plt.figure(figsize=(12, 6))  # Größe des Diagramms festlegen
    sns.heatmap(
        heatmap_data,  # Die erstellte Pivot-Tabelle als Datenquelle
        cmap="coolwarm",  # Farbskala: Blau für wenig, Rot für viele Sichtungen
        annot=False,  # Keine Werte direkt in die Zellen schreiben (kann auf True gesetzt werden)
        linewidths=0.5  # Feine Linien zwischen den Zellen für bessere Lesbarkeit
    )

    # Diagrammbeschriftung hinzufügen
    plt.xlabel("Jahr")  # X-Achsen-Beschriftung
    plt.ylabel("Stunde des Tages")  # Y-Achsen-Beschriftung
    plt.title("Heatmap der UFO-Sichtungen in Area 51 (Jahr vs. Stunde)")  # Titel der Heatmap

    plt.savefig("heatmap.png")
    plt.show()
