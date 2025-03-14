import folium
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap
import pandas as pd
import os
import filter_by_dates
import haversine

def create_cluster_heat_map(df:pd.DataFrame,
                            filename:str, 
                            main_dir, 
                            start_date:str = None, 
                            end_date:str   = None,  
                            radius:int     = None, 
                            map_type:str   = "cluster"
                           ) -> None:
    """Erstellt eine Cluster Map mit map_type = "cluster",
    eine OPNV Map mit map_type ="opnv 
    oder eine Heat Map mit map_type = "heat" mit Folium.
    Dabei kann optional ein Datetime Intervall und ein Radius um Cape Caneveral angegeben werden.
    Die fertige Map wird im Ordner 'main_dir'/data/data_map mit dem namen 'filename'.hmtl abgelegt"""

    # Zeitliches Interval:
    if start_date or end_date:
        df = filter_by_dates.filter_by_interval(df, start_date, end_date)

    # Radius:

    if radius:
        distances = haversine.distance(28.3922, -80.6077, df["latitude"], df["longitude"])  # Fixpunkt ist Cape Caneveral
        df = df[distances <= radius]

    center_lat = df["latitude"].mean()
    center_lon = df["longitude"].mean()

    map = folium.Map(location=[center_lat, center_lon], zoom_start = 5)

    folium.Marker(location = [28.3922, -80.6077],                                   # Cape Canaveral Koordinaten
                  popup    = "🚀 Cape Canaveral Spaceport",
                  icon     = folium.Icon(color="red", icon="rocket", prefix="fa")   # Rotes Symbol mit Rakete
                 ).add_to(map)
    
    if map_type == "heat":                                                          # für Hitzkarte
            
            map_data = list(zip(df["latitude"], df["longitude"]))
            HeatMap(map_data).add_to(map)

    if map_type == "cluster" or map_type == "opnv":                                 # cluster map or cluster opnv map
                                 
        marker_cluster = MarkerCluster().add_to(map)

        for lat, lon in zip(df["latitude"], df["longitude"]):
            folium.Marker([lat, lon]).add_to(marker_cluster)    

        if map_type == "opnv":
             folium.TileLayer(tiles = "https://tile.memomaps.de/tilegen/{z}/{x}/{y}.png",
                              attr  = "© OpenStreetMap-Mitwirkende, Memomaps",
                              name  = "ÖPNV-Karte"
                             ).add_to(map)
             folium.LayerControl().add_to(map)
    
    map_filename = f"{filename}.html" 
    path_to_data_map = os.path.join(main_dir, "data", "data_map", map_filename)     # wo soll die map gespeichert werden
    map.save(path_to_data_map)                                                      # Speichern der map mit map_filename