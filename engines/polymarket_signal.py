from api.polymarket import get_active_markets

def detect_anomalies() -> list:
    markets = get_active_markets()
    anomalies = []
    
    for market in markets:
        volume = float(market.get('volume', 0))
        if volume > 100000:
            title = market.get('title', 'Unknown Market')
            anomalies.append({
                "Market": title,
                "Volume": f"${volume:,.2f}",
                "Signal": "High Volume Detected"
            })
            
    return anomalies[:5]
