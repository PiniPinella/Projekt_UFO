import os
import subprocess
import logging
import time

start_time = time.time()                                                        # Timestamp für Zeitmessung

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))                           # Pfad des ROOT Verzeichnisses bestimmen  

#############################
# Erstelle zentralen Logger
#############################

LOG_DIR = os.path.join(ROOT_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok = True)                                           # Erstellt Ordner "logs"
logging.basicConfig(filename = os.path.join(LOG_DIR, "script_log.log"),         # Log-Datei script_log.log
                    level    = logging.DEBUG,                                   # Level: DEBUG, INFO, WARNING, ERROR, CRITICAL
                    format   = "%(asctime)s - %(levelname)s - %(message)s",     # Legt Message Format fest
                    datefmt  = "%d/%m/%Y %H:%M:%S"                              # Legt Datetime Format fest
                   )

logger = logging.getLogger(__name__)                                            # Logger einfacher verfügbar machen für andere Skripte
logger.info("main.py gestartet.")                                               # Logt Informationen in der zentralen Log-Datei

#############################
# Skripts
#############################

# Starte data_cleanup_script
try:                                                                                            # Try, Except für Fehler
    path_to_data_cleanup_script = os.path.join(ROOT_DIR, "scripts", "data_cleanup_script.py")   # Pfad zum Skript
    print("data_cleanup_script Skript startet.")                                                
    logger.info("data_cleanup_script Skript startet.")                          
    subprocess.run(["python", path_to_data_cleanup_script, ROOT_DIR],   # Startet das Skript 'data_cleanup_script.py' und übergibt ROOT_DIR als arg. 
                   check = True, capture_output = True, text = True     # check = true löst Exception aus, wenn das Skript fehlschlägt
                  )                                                     # stdout und stderr werden aufgefangen und zu Text dekodiert                
    print("data_cleanup Skript abgeschlossen.")
    logger.info("data_cleanup Skript abgeschlossen.")
except subprocess.CalledProcessError as e:                                                      # falls Skript fehlschlägt
    logger.error(f"Fehler beim ausführen von 'data_cleanup_script': {e}", exc_info = True)      # Logt Fehler in der zentralen Log-Datei mit Traceback
    logger.error(f"Fehlerausgabe (stderr): {e.stderr}")                                         # Fängt die genaue Fehlermeldung aus dem Subprocess ab

# Starte datetime_analysis_script
try:
    path_to_datetime_analysis_script = os.path.join(ROOT_DIR, "scripts", "datetime_analysis_script.py")
    print("datetime_analysis_script Skript startet.")
    logger.info("datetime_analysis_script Skript startet.")
    subprocess.run(["python", path_to_datetime_analysis_script, ROOT_DIR],
                   check = True, capture_output = True, text = True     
                  )
    print("datetime_analysis_script  Skript abgeschlossen.")
    logger.info("datetime_analysis_script  Skript abgeschlossen.")
except subprocess.CalledProcessError as e:
    logger.error(f"Fehler beim ausführen von 'datetime_analysis_script': {e}", exc_info = True)
    logger.error(f"Fehlerausgabe (stderr): {e.stderr}")   

# Starte duration_analysis_script
try:
    path_to_duration_analysis_script = os.path.join(ROOT_DIR, "scripts", "duration_analysis_script.py")
    print("duration_analysis_script Skript startet.")
    logger.info("duration_analysis_script Skript startet.")
    subprocess.run(["python", path_to_duration_analysis_script, ROOT_DIR],
                   check = True, capture_output = True, text = True     
                  )
    print("duration_analysis_script  Skript abgeschlossen.")
    logger.info("duration_analysis_script  Skript abgeschlossen.")
except subprocess.CalledProcessError as e:
    logger.error(f"Fehler beim ausführen von 'duration_analysis_script': {e}", exc_info = True)
    logger.error(f"Fehlerausgabe (stderr): {e.stderr}") 

# Starte area51_analsis_script
try:
    path_to_area51_analysis_script = os.path.join(ROOT_DIR, "scripts", "area51_analysis_script.py")
    print("area51_analysis_script Skript startet.")
    logger.info("area51_analysis_script Skript startet.")
    subprocess.run(["python", path_to_area51_analysis_script, ROOT_DIR],
                   check = True, capture_output = True, text = True     
                  )
    print("area51_analysis_script  Skript abgeschlossen.")
    logger.info("area51_analysis_script  Skript abgeschlossen.")
except subprocess.CalledProcessError as e:
    logger.error(f"Fehler beim ausführen von 'area51_analysis_script': {e}", exc_info = True)
    logger.error(f"Fehlerausgabe (stderr): {e.stderr}")

# Starte geo_analysis_script
try:
    path_to_geo_analysis_script = os.path.join(ROOT_DIR, "scripts", "geo_analysis_script.py")
    print("geo_analysis_script Skript startet.")
    logger.info("geo_analysis_script Skript startet.")
    subprocess.run(["python", path_to_geo_analysis_script, ROOT_DIR],
                   check = True, capture_output = True, text = True     
                  )
    print("geo_analysis_script  Skript abgeschlossen.")
    logger.info("geo_analysis_script  Skript abgeschlossen.")
except subprocess.CalledProcessError as e:
    logger.error(f"Fehler beim ausführen von 'geo_analysis_script': {e}", exc_info = True)
    logger.error(f"Fehlerausgabe (stderr): {e.stderr}") 

# Starte shape_analysis_script
try:
    path_to_shape_analysis_script = os.path.join(ROOT_DIR, "scripts", "shape_analysis_script.py")
    print("shape_analysis_script Skript startet.")
    logger.info("shape_analysis_script Skript startet.")
    subprocess.run(["python", path_to_shape_analysis_script, ROOT_DIR],
                   check = True, capture_output = True, text = True     
                  )
    print("shape_analysis_script  Skript abgeschlossen.")
    logger.info("shape_analysis_script  Skript abgeschlossen.")
except subprocess.CalledProcessError as e:
    logger.error(f"Fehler beim ausführen von 'shape_analysis_script': {e}", exc_info = True)
    logger.error(f"Fehlerausgabe (stderr): {e.stderr}") 
    
#############################
# Zusammenfassungen
#############################
# png zieher



end_time = time.time()
elapsed_time = end_time - start_time
logger.info(f"Skriptlaufzeit: {elapsed_time:.2f} Sekunden")
print(f"Skriptlaufzeit: {elapsed_time:.2f} Sekunden")