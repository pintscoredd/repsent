from api.news import get_top_news

def assess_geo_risk(region: str) -> dict:
    articles = get_top_news(f"geopolitics {region} conflict")
    risk_score = 0
    keywords = ['war', 'strike', 'escalation', 'troops', 'sanctions', 'missile', 'tension']
    
    for article in articles:
        text = str(article.get('title', '')) + " " + str(article.get('description', ''))
        text = text.lower()
        for kw in keywords:
            if kw in text:
                risk_score += 1

    level = "LOW"
    if risk_score > 15:
        level = "CRITICAL"
    elif risk_score > 5:
        level = "ELEVATED"
        
    return {
        "Region": region,
        "Risk Level": level,
        "Score": risk_score,
        "Articles Scanned": len(articles)
    }
