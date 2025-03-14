import pandas as pd

def filter_by_interval(df:pd.DataFrame, start_date:str = None, end_date:str = None) ->pd.DataFrame:
    """Sortiert und gibt einen Ufo-DataFrame in einem Datetime-Intervall zurück.
    start_date, end_date im ISO-Format yyyy-mm-dd."""

    df["datetime"] = pd.to_datetime(df["datetime"])  # YYYY-MM-DD ist default

    date1 = pd.to_datetime(start_date) if start_date else df["datetime"].min()
    date2 = pd.to_datetime(end_date) if end_date else df["datetime"].max()

    filtered_df = df[(df["datetime"] >= date1) & (df["datetime"] <= date2)]
    filtered_df = filtered_df.sort_values(by="datetime")

    return filtered_df