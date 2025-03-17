import os
import sys

ROOT_DIR = sys.argv[1]
sys.path.append(ROOT_DIR)

from functions import create_map
from functions import ufo_df_loader

path_to_data_map = os.path.join(ROOT_DIR, "data", "data_map")
path_to_data_clean_read = os.path.join(ROOT_DIR, "data", "data_clean", "ufo_sightings_scrubbed_clean.csv")

ufo_df = ufo_df_loader.load_ufo_df(path_to_data_clean_read)

create_map.create_cluster_heat_map(ufo_df, "testmap", ROOT_DIR, radius=1000, map_type="cluster")