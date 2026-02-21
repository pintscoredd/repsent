import streamlit as st
import pandas as pd
from engines.polymarket_signal import detect_anomalies
from utils.time import get_pst_time

def execute_poly(topic: str):
    title = f"POLYMARKET ANOMALY DETECTION: {topic.upper()}" if topic else "POLYMARKET ANOMALY DETECTION"
    st.header(title)
    st.caption(get_pst_time())
    
    with st.spinner("Scanning active Polymarket contracts..."):
        try:
            anomalies = detect_anomalies()
            if not anomalies:
                st.info("No volume anomalies detected right now.")
                return
                
            df = pd.DataFrame(anomalies)
            st.dataframe(df, use_container_width=True, hide_index=True)
        except Exception as e:
            st.error(f"Error fetching polymarket data: {e}")
