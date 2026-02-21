from utils.formatting import print_header, console
from engines.ripple_engine import compute_ripple_effects

def execute_scenario(event: str):
    print_header(f"SCENARIO ANALYSIS: {event.upper()}")
    ripples = compute_ripple_effects(event)
    for r in ripples:
        console.print(f"[bold cyan]{r}[/bold cyan]")
