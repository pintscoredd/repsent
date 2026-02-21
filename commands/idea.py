import streamlit as st
from engines.historical_engine import find_analog
from api.yahoo import get_price_history
from utils.time import get_pst_time

def execute_idea(theme: str):
    st.header(f"TRADE IDEA GENERATOR: {theme.upper()}")
    st.caption(get_pst_time())
    
    if theme.upper() == "SPY":
        with st.spinner("Analyzing historical analogs..."):
            df = get_price_history("SPY", period="3mo", interval="1d")
            if not df.empty:
                trend = df['Close'].pct_change().dropna().tolist()
                analog = find_analog("SPY", trend)
                st.success(f"Nearest Historical Analog for SPY: **{analog}**")
            else:
                st.warning("Could not fetch SPY data for analog analysis.")
    else:
        st.info(f"Generating thesis for theme: **{theme}**...")
        st.write("Recommend checking Scenario and Polymarket tabs for convergence.")
