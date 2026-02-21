import sys
import os

# Ensure the root directory is in the Python path for cloud deployments
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import typer
from commands.brief import execute_brief
from commands.flash import execute_flash
from commands.scenario import execute_scenario
from commands.geo import execute_geo
from commands.rotate import execute_rotate
from commands.sentiment import execute_sentiment
from commands.idea import execute_idea
from commands.poly import execute_poly

app = typer.Typer(help="SENTINEL - Macro Intelligence Terminal", no_args_is_help=True)

@app.command()
def brief():
    execute_brief()

@app.command()
def flash(ticker: str):
    execute_flash(ticker)

@app.command()
def scenario(asset: str):
    execute_scenario(asset)

@app.command()
def geo(region: str):
    execute_geo(region)

@app.command()
def rotate():
    execute_rotate()

@app.command()
def sentiment():
    execute_sentiment()

@app.command()
def idea(theme: str):
    execute_idea(theme)

@app.command()
def poly(topic: str = ""):
    execute_poly(topic)

if __name__ == "__main__":
    app()
