import streamlit as st
from engines.geo_engine import assess_geo_risk
from utils.time import get_pst_time

def execute_geo(region: str):
    st.header(f"GEO RISK ASSESSMENT: {region.upper()}")
    st.caption(get_pst_time())
    
    with st.spinner("Scanning geopolitical news..."):
        try:
            risk = assess_geo_risk(region)
            st.subheader(f"Risk Level: {risk['Risk Level']}")
            st.write(f"**Score:** {risk['Score']}")
            st.write(f"**Articles Scanned:** {risk['Articles Scanned']}")
            
            if risk["Risk Level"] == "CRITICAL":
                st.error("CRITICAL RISK DETECTED")
            elif risk["Risk Level"] == "ELEVATED":
                st.warning("ELEVATED RISK DETECTED")
            else:
                st.success("LOW RISK")
        except Exception as e:
            st.error(f"Error fetching geo risk: {e}")
