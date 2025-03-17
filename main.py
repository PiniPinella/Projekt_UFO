import os
import subprocess

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Starte data_cleanup_script
path_to_data_cleanup_script = os.path.join(ROOT_DIR, "scripts", "data_cleanup_script.py")
print("data_cleanup Skript startet.")
subprocess.run(["python", path_to_data_cleanup_script, ROOT_DIR])
print("data_cleanup Skript abgeschlossen.")

# Starte datetime_analysis_script

# Starte duration_analysis_script

# Starte area51_analsis_script

# Starte geo_analysis_script

# Starte shape_analysis_script

# usw...