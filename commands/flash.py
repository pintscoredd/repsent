from utils.formatting import print_header, console
from api.yahoo import get_price_history
from rich.panel import Panel

def execute_flash(ticker: str):
    print_header(f"FLASH ANALYSIS: {ticker.upper()}")
    df = get_price_history(ticker, period="1mo", interval="1d")
    if df.empty:
        return
        
    start_price = df['Close'].iloc[0]
    end_price = df['Close'].iloc[-1]
    change = ((end_price - start_price) / start_price) * 100
    
    color = "green" if change >= 0 else "red"
    console.print(Panel(f"30-Day Performance: [{color}]{change:.2f}%[/{color}]\nCurrent Price: ${end_price:.2f}", title=ticker.upper()))
