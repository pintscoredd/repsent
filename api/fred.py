import requests
import pandas as pd
from config import config
from utils.error_handling import handle_api_error, handle_missing_key

def get_fred_series(series_id: str, limit: int = 100) -> pd.DataFrame:
    if not config.FRED_API_KEY:
        handle_missing_key("FRED", "FRED_API_KEY")
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={series_id}&api_key={config.FRED_API_KEY}&file_type=json&limit={limit}&sort_order=desc"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        observations = data.get("observations", [])
        if not observations:
            return pd.DataFrame()
        df = pd.DataFrame(observations)
        df['value'] = pd.to_numeric(df['value'], errors='coerce')
        df['date'] = pd.to_datetime(df['date'])
        df = df.dropna(subset=['value'])
        return df[['date', 'value']].sort_values('date').reset_index(drop=True)
    except Exception as e:
        handle_api_error("FRED", str(e))
        return pd.DataFrame()
