from utils.formatting import print_header, console
from api.news import get_top_news

def execute_sentiment():
    print_header("MACRO SENTIMENT ANALYSIS")
    articles = get_top_news("global macro markets")
    if not articles:
        return
        
    for i, a in enumerate(articles[:5], 1):
        console.print(f"[bold white]{i}. {a.get('title')}[/bold white]")
        console.print(f"[dim]{a.get('source', {}).get('name')} - {a.get('publishedAt')}[/dim]\n")
