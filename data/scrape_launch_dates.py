from bs4 import BeautifulSoup
import os
import pandas as pd
import sys

print("scrape_launch_dates gestartet.")

ROOT_DIR = sys.argv[1]

path_to_data_raw = os.path.join(ROOT_DIR, "data", "data_raw", "htm")      # Ordner mit HTML-Dateien

all_dates = []

print("Scraping beginnt.")

for filename in os.listdir(path_to_data_raw):
    if filename.endswith(".htm"):
        with open(os.path.join(path_to_data_raw, filename), "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "lxml")
            date_cells = soup.find_all("td", class_="column-1")
            dates = [cell.get_text(strip=True) for cell in date_cells]
            all_dates.extend(dates)

print("Scraping endet.")

launch_dates_df = pd.DataFrame(all_dates, columns=["launch_dates"])

launch_dates_clean_path = os.path.join(ROOT_DIR, "data", "data_clean", "cape_canaveral_launch_chronology.csv")
launch_dates_df.to_csv(launch_dates_clean_path, index=False)
print(f"Bereinigte CSV-Datei erstellt: {launch_dates_clean_path}")

print("scrape_launch_dates beendet.")