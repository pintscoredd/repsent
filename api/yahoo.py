import yfinance as yf
import pandas as pd
from utils.error_handling import handle_api_error

def get_price_history(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    try:
        t = yf.Ticker(ticker)
        df = t.history(period=period, interval=interval)
        if df.empty:
            handle_api_error("Yahoo Finance", f"No data found for ticker {ticker}")
        return df
    except Exception as e:
        handle_api_error("Yahoo Finance", str(e))
        return pd.DataFrame()

def get_current_price(ticker: str) -> float:
    df = get_price_history(ticker, period="1d")
    if not df.empty:
        return float(df['Close'].iloc[-1])
    return 0.0
