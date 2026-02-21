import pandas as pd
from api.yahoo import get_price_history
from api.coingecko import get_crypto_history
import concurrent.futures

def compute_rolling_correlations() -> pd.DataFrame:
    assets = {
        'DXY': 'DX-Y.NYB',
        'Gold': 'GC=F',
        '10Y Yield': '^TNX',
        'SPY': 'SPY'
    }
    
    data = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_asset = {executor.submit(get_price_history, ticker, "1y", "1d"): name for name, ticker in assets.items()}
        future_crypto = executor.submit(get_crypto_history, "bitcoin", 365)
        
        for future in concurrent.futures.as_completed(future_to_asset):
            name = future_to_asset[future]
            df = future.result()
            if not df.empty:
                df.index = pd.to_datetime(df.index).tz_localize(None)
                data[name] = df['Close']
                
        crypto_df = future_crypto.result()
        if not crypto_df.empty:
            crypto_df.set_index('date', inplace=True)
            crypto_df.index = pd.to_datetime(crypto_df.index).tz_localize(None)
            data['BTC'] = crypto_df['price']

    prices = pd.DataFrame(data).dropna()
    returns = prices.pct_change().dropna()
    correlations = returns.rolling(window=60).corr().dropna()
    if not correlations.empty:
        return correlations.iloc[-len(returns.columns):]
    return pd.DataFrame()
