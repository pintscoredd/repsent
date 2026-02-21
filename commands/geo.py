from utils.formatting import print_header, console
from engines.geo_engine import assess_geo_risk
from rich.panel import Panel

def execute_geo(region: str):
    print_header(f"GEO RISK ASSESSMENT: {region.upper()}")
    risk = assess_geo_risk(region)
    color = "red" if risk["Risk Level"] == "CRITICAL" else "yellow" if risk["Risk Level"] == "ELEVATED" else "green"
    
    text = f"Risk Level: [{color}]{risk['Risk Level']}[/{color}]\nScore: {risk['Score']}\nArticles Scanned: {risk['Articles Scanned']}"
    console.print(Panel(text, title=f"{region.upper()} RISK"))
