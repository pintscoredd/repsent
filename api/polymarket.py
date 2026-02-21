import requests
from utils.error_handling import handle_api_error

def get_active_markets() -> list:
    url = "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=50"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        handle_api_error("Polymarket", str(e))
        return []

def get_market_volume_data(market_id: str) -> dict:
    url = f"https://gamma-api.polymarket.com/events/{market_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        handle_api_error("Polymarket", str(e))
        return {}
