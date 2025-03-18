import os
import subprocess

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Starte data_cleanup_script
path_to_data_cleanup_script = os.path.join(ROOT_DIR, "scripts", "data_cleanup_script.py")
print("data_cleanup_script Skript startet.")
# subprocess.run(["python", path_to_data_cleanup_script, ROOT_DIR])
print("data_cleanup Skript abgeschlossen.")

# Starte datetime_analysis_script
path_to_datetime_analysis_script = os.path.join(ROOT_DIR, "scripts", "datetime_analysis_script.py")
print("datetime_analysis_script Skript startet.")
# subprocess.run(["python", path_to_datetime_analysis_script, ROOT_DIR])
print("datetime_analysis_script  Skript abgeschlossen.")

# Starte duration_analysis_script
path_to_duration_analysis_script = os.path.join(ROOT_DIR, "scripts", "duration_analysis_script.py")
print("duration_analysis_script Skript startet.")
# subprocess.run(["python", path_to_duration_analysis_script, ROOT_DIR])
print("duration_analysis_script  Skript abgeschlossen.")

# Starte area51_analsis_script
path_to_area51_analysis_script = os.path.join(ROOT_DIR, "scripts", "area51_analysis_script.py")
print("area51_analysis_script Skript startet.")
subprocess.run(["python", path_to_area51_analysis_script, ROOT_DIR])
print("area51_analysis_script  Skript abgeschlossen.")

# Starte geo_analysis_script
path_to_geo_analysis_script = os.path.join(ROOT_DIR, "scripts", "geo_analysis_script.py")
print("geo_analysis_script Skript startet.")
# subprocess.run(["python", path_to_geo_analysis_script, ROOT_DIR])
print("geo_analysis_script  Skript abgeschlossen.")

# Starte shape_analysis_script
path_to_shape_analysis_script = os.path.join(ROOT_DIR, "scripts", "shape_analysis_script.py")
print("shape_analysis_script Skript startet.")
# subprocess.run(["python", path_to_shape_analysis_script, ROOT_DIR])
print("shape_analysis_script  Skript abgeschlossen.")

# usw...