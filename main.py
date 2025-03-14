import os
import subprocess

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# Starte data_cleanup.py
path_to_data_cleanup_script = os.path.join(ROOT_DIR, "data", "data_cleanup.py")
print("data_cleanup Skript startet.")
subprocess.run(["python", path_to_data_cleanup_script, ROOT_DIR])
print("data_cleanup Skript abgeschlossen.")

# Starte scrape_launch_dates.py
path_to_scrape_launch_dates = os.path.join(ROOT_DIR, "data", "scrape_launch_dates.py")
print("scrape_launch_dates Skript startet.")
subprocess.run(["python", path_to_scrape_launch_dates, ROOT_DIR])
print("scrape_launch_dates Skript abgeschlossen.")

# Starte extract_comments.py
path_to_extract_comments = os.path.join(ROOT_DIR, "comments_analysis", "extract_comments.py")
print("extract_comments Skript startet.")
subprocess.run(["python", path_to_extract_comments, ROOT_DIR])
print("extract_comments Skript abgeschlossen.")

# usw...