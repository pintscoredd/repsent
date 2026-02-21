import streamlit as st
import pandas as pd
from engines.cross_asset import compute_rolling_correlations
from utils.time import get_pst_time

def execute_rotate():
    st.header("CROSS-ASSET ROTATION & CORRELATION (60-DAY)")
    st.caption(get_pst_time())
    
    with st.spinner("Computing 60-day rolling correlations..."):
        corr = compute_rolling_correlations()
        if corr.empty:
            st.warning("No correlation data available.")
            return
            
        corr = corr.reset_index()
        columns = ["Asset"] + list(corr.columns[1:])
        
        for col in corr.columns[1:]:
            corr[col] = pd.to_numeric(corr[col], errors='coerce').round(2)
            
        st.dataframe(corr, use_container_width=True, hide_index=True)
