import pandas as pd


# Zeile datetime in Datetime-Format umwandeln
def clean_datetime_column(df, datetime_column="datetime"):
    datetime_clean = pd.to_datetime(df[datetime_column], format="mixed", errors="coerce")
    return datetime_clean



# Jahreszeiten filtern
def get_season(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "sommer"
    else:
        return "autumn"