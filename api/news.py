import requests
from config import config
from utils.error_handling import handle_api_error, handle_missing_key

def get_top_news(query: str = "macro economy") -> list:
    if not config.NEWS_API_KEY:
        handle_missing_key("NewsAPI", "NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&pageSize=10&apiKey={config.NEWS_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("articles", [])
    except Exception as e:
        handle_api_error("NewsAPI", str(e))
        return []
