import pandas as pd
from pathlib import Path

def read_csv(airport:str):
    csv_busy_times = Path("./data/"+ airport + "/busy_times.csv")
    csv_flights = Path("./data/" + airport + "/flights_processed.csv")

    df_csv_busy_times = pd.read_csv(csv_busy_times)
    df_csv_flights = pd.read_csv(csv_flights)
    
    return df_csv_busy_times, df_csv_flights

def export_html(df_html_busy_times, df_html_flights, airport:str):
    html_busy_times = Path("./data/" + airport + "/busy_times.html")
    html_flights = Path("./data/" + airport + "/flights_processed.html")

    df_html_busy_times.to_html(html_busy_times)
    df_html_flights.to_html(html_flights)
    
def convert_csv_to_html(airport:str):
    df_csv_busy_times,  df_csv_flights = read_csv(airport)
    
    export_html(df_csv_busy_times, df_csv_flights, airport)
    
if __name__ == "__main__":
    default_airport = "cork"
    convert_csv_to_html(default_airport)
