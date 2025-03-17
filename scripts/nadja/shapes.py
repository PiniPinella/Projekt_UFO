# Importe
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

##### DATENSATZ-ZIEHEN #####
##############################

# Anzeige der Spaltennamen
ufo_df.columns
##############################################

## Sichtungsdauer je Form analysieren

# Vorbereitung
# Spalte "Shape" in Strings formatieren 

print(ufo_df['shape'].dtype)
shape_string = ufo_df.iloc[:, 5].astype("string")
shape_string

# --------------------------

# Überprüfen, welcher Datentyp in Spalte duration_seconds
print(ufo_df['duration_seconds'].dtype)

# Gruppierung der Sichtungsform und Berechnung der durchschn. Dauer
average_duration = ufo_df.groupby("shape")["duration_seconds"].mean().reset_index()

# Sortierung nach duration_seconds
average_duration_sorted = average_duration.sort_values(by="duration_seconds", ascending=False)

average_duration_sorted


# Plot erstellen -- Durchschnittliche Dauer von UFO-Sichtungen nach Form
average_duration_sorted.plot(
    kind= "bar",        # Diagrammtyp
    figsize= (10, 6),     # Größe des Diagrammes festlegen
    x= "shape",             # x-Achse
    y= "duration_seconds"
)



plt.title("Durchschnittliche Dauer von UFO-Sichtungen nach Form", fontsize=16, fontweight='bold')  # Titel anpassen
plt.xlabel("Sichtungsform", fontsize=14)               # x-Achsen-Beschriftung anpassen
plt.ylabel("Dauer in Sekunden", fontsize=14)  # y-Achsen-Beschriftung anpassen
plt.xticks(rotation=45)                         # Drehen der Beschriftung
plt.tight_layout()                              # Optimiert das Layout
plt.grid(axis='y', linestyle='--', alpha=0.7)   # Gitterlinien für die y-Achse
plt.gca().xaxis.grid(False)                     # Deaktiviert Gitternetzlinien auf der x-Achse


# Diagramm anzeigen
plt.show

##############################################
# Dauer der Sichtung je Form in Summe

# Aggregiere die Dauer in Sekunden je Form
duration_by_shape = ufo_df.groupby('shape')['duration_seconds'].sum().reset_index()

# Sortierung nach duration_seconds
average_duration_sorted_sum = duration_by_shape.sort_values(by="duration_seconds", ascending=False)

average_duration_sorted_sum

duration_by_shape = pd.DataFrame(duration_by_shape)

# Balkendiagramm erstellen
plt.figure(figsize=(12, 8))
sns.barplot(data=duration_by_shape, x='shape', y='duration_seconds', palette='viridis')

# Diagrammtitel und Achsenbeschriftungen
plt.title("Average Duration of UFO Sightings by Shape", fontsize=16)
plt.xlabel("Shapes", fontsize=14)
plt.ylabel("Duration in Seconds", fontsize=14)

# Achsenanpassungen
plt.xticks(rotation=45)
plt.tight_layout()

# Diagramm anzeigen
plt.show()
