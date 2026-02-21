from utils.formatting import print_header, console
from engines.historical_engine import find_analog
from api.yahoo import get_price_history

def execute_idea(theme: str):
    print_header(f"TRADE IDEA GENERATOR: {theme.upper()}")
    if theme.upper() == "SPY":
        df = get_price_history("SPY", period="3mo", interval="1d")
        if not df.empty:
            trend = df['Close'].pct_change().dropna().tolist()
            analog = find_analog("SPY", trend)
            console.print(f"Nearest Historical Analog for SPY: [bold magenta]{analog}[/bold magenta]")
    else:
        console.print(f"Generating thesis for theme: [bold]{theme}[/bold]...")
        console.print("Recommend checking /scenario and /poly for convergence.")
