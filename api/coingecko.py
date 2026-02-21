import requests
import pandas as pd
from utils.error_handling import handle_api_error

def get_crypto_price(coin_id: str) -> float:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return float(data.get(coin_id, {}).get("usd", 0.0))
    except Exception as e:
        handle_api_error("CoinGecko", str(e))
        return 0.0

def get_crypto_history(coin_id: str, days: int = 60) -> pd.DataFrame:
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days={days}&interval=daily"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        prices = data.get("prices", [])
        df = pd.DataFrame(prices, columns=['timestamp', 'price'])
        df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df[['date', 'price']].sort_values('date')
    except Exception as e:
        handle_api_error("CoinGecko", str(e))
        return pd.DataFrame()
