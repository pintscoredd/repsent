import sys
import os
import streamlit as st

# Ensure the root directory is in the Python path for cloud deployments
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from commands.brief import execute_brief
from commands.flash import execute_flash
from commands.scenario import execute_scenario
from commands.geo import execute_geo
from commands.rotate import execute_rotate
from commands.sentiment import execute_sentiment
from commands.idea import execute_idea
from commands.poly import execute_poly

st.set_page_config(page_title="SENTINEL Macro", layout="wide", page_icon="🌐")

st.sidebar.title("SENTINEL Terminal")
st.sidebar.markdown("Macro Intelligence Dashboard")

page = st.sidebar.radio("Navigation", [
    "Brief", "Flash", "Scenario", "Geo", "Rotate", "Sentiment", "Idea", "Polymarket"
])

if page == "Brief":
    execute_brief()
elif page == "Flash":
    ticker = st.text_input("Ticker", value="SPY")
    if st.button("Run Flash Analysis"):
        execute_flash(ticker)
elif page == "Scenario":
    event = st.text_input("Macro Event", value="Rate Cut")
    if st.button("Run Scenario Simulation"):
        execute_scenario(event)
elif page == "Geo":
    region = st.text_input("Region", value="Middle East")
    if st.button("Assess Geopolitical Risk"):
        execute_geo(region)
elif page == "Rotate":
    if st.button("Load Cross-Asset Rotation"):
        execute_rotate()
elif page == "Sentiment":
    if st.button("Fetch Macro Sentiment"):
        execute_sentiment()
elif page == "Idea":
    theme = st.text_input("Theme", value="SPY")
    if st.button("Generate Trade Idea"):
        execute_idea(theme)
elif page == "Polymarket":
    topic = st.text_input("Topic (Optional)")
    if st.button("Detect Anomalies"):
        execute_poly(topic)
