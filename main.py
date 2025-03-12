import os
import subprocess

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Starte data_cleanup.ipynb
path_to_data_cleanup_script = os.path.join(ROOT_DIR, "data", "data_cleanup.py")
print("data_cleanup Skript startet")
subprocess.run(["python", path_to_data_cleanup_script, ROOT_DIR])
print("data_cleanup Skript abgeschlossen")

# Starte laura_script usw. ...