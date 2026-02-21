import streamlit as st
from engines.ripple_engine import compute_ripple_effects
from utils.time import get_pst_time

def execute_scenario(event: str):
    st.header(f"SCENARIO ANALYSIS: {event.upper()}")
    st.caption(get_pst_time())
    
    ripples = compute_ripple_effects(event)
    for r in ripples:
        st.info(r)
