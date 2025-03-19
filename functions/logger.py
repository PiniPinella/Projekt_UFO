import os
import logging

folder = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.abspath(os.path.join(folder, ".."))
LOG_DIR = os.path.join(ROOT_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok = True)                                           # Erstellt Ordner "logs"
logging.basicConfig(filename = os.path.join(LOG_DIR, "script_log.log"),         # Log-Datei script_log.log
                    level    = logging.DEBUG,                                   # Level: DEBUG, INFO, WARNING, ERROR, CRITICAL
                    format   = "%(asctime)s - %(levelname)s - %(message)s",     # Legt Message Format fest
                    datefmt  = "%d/%m/%Y %H:%M:%S"                              # Legt Datetime Format fest
                   )

logger = logging.getLogger(__name__)                                            # Logger einfacher verfügbar machen für andere Skripte