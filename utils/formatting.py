from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from utils.time import get_pst_time

console = Console()

def print_header(title: str):
    console.print(Panel(f"[bold cyan]{title}[/bold cyan] | [dim]{get_pst_time()}[/dim]"))

def print_table(title: str, columns: list, rows: list):
    table = Table(title=title, show_header=True, header_style="bold magenta")
    for col in columns:
        table.add_column(col)
    for row in rows:
        table.add_row(*[str(r) for r in row])
    console.print(table)
