def compute_ripple_effects(event: str) -> list:
    event_lower = event.lower()
    if "rate cut" in event_lower:
        return [
            "1. Treasury yields decline across the curve.",
            "2. USD weakens against major pairs (EUR, JPY).",
            "3. Gold and non-yielding assets catch bids.",
            "4. Long-duration tech and growth equities rally.",
            "5. Emerging market debt spreads compress."
        ]
    elif "inflation" in event_lower or "cpi" in event_lower:
        return [
            "1. Rate hike expectations get priced in.",
            "2. USD catches a strong bid.",
            "3. Yields spike, pressuring equity valuations.",
            "4. Commodities may rally if structural.",
            "5. Consumer discretionary underperforms."
        ]
    elif "war" in event_lower or "geopolitical" in event_lower:
        return [
            "1. Immediate bid for safe havens (Gold, CHF, USD).",
            "2. Brent crude and energy markets gap up.",
            "3. High-beta equities sell off sharply.",
            "4. Volatility (VIX) spikes, leading to forced deleveraging.",
            "5. Supply chain sensitive sectors underperform."
        ]
    else:
        return [
            "1. Baseline volatility increase.",
            "2. Algorithmic sentiment tracking adjusts.",
            "3. Market awaits further macro confirmation."
        ]
