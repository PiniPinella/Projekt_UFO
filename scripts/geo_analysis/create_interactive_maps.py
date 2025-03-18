import os
import sys


if len(sys.argv) > 1:
    ROOT_DIR = sys.argv[1]
else:
    folder = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.abspath(os.path.join(folder, "..", ".."))
print(ROOT_DIR)
sys.path.append(ROOT_DIR)

from functions import create_map
from functions import ufo_df_loader

path_to_data_map = os.path.join(ROOT_DIR, "data", "data_map")
path_to_data_clean_read = os.path.join(ROOT_DIR, "data", "data_clean", "ufo_sightings_scrubbed_clean.csv")

ufo_df = ufo_df_loader.load_ufo_df(path_to_data_clean_read)

# Leoniden 16./17. Nov 1999 Cluster Map
create_map.create_cluster_heat_map(ufo_df, 
                                   filename   = "Leoniden_1617_11_1999_Cluster", 
                                   main_dir   = ROOT_DIR, 
                                   start_date = "1999-11-16", 
                                   end_date   = "1999-11-17", 
                                   map_type   = "cluster"
                                  )
print("map1 fertig")
# Leoniden 16./17. Nov 1999 Heat Map
create_map.create_cluster_heat_map(ufo_df, 
                                   filename   = "Leoniden_1617_11_1999_Heat", 
                                   main_dir   = ROOT_DIR, 
                                   start_date = "1999-11-16", 
                                   end_date   = "1999-11-17", 
                                   map_type   = "heat"
                                  )
print("map2 fertig")
# Independence Day 04. Jul 2010
create_map.create_cluster_heat_map(ufo_df, 
                                   filename   = "Independence_Day_04_07_2010_cluster", 
                                   main_dir   = ROOT_DIR, 
                                   start_date = "2010-07-04", 
                                   end_date   = "2010-07-04", 
                                   map_type   = "cluster"
                                  )
print("map3 fertig")

