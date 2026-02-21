import streamlit as st
import pandas as pd
from api.yahoo import get_current_price
from api.coingecko import get_crypto_price
from utils.time import get_pst_time

def execute_brief():
    st.header("SENTINEL MACRO BRIEF")
    st.caption(get_pst_time())
    
    spy = get_current_price("SPY")
    dxy = get_current_price("DX-Y.NYB")
    tnx = get_current_price("^TNX")
    gold = get_current_price("GC=F")
    btc = get_crypto_price("bitcoin")
    
    data = [
        ["SPY", f"${spy:.2f}"],
        ["DXY", f"{dxy:.2f}"],
        ["10Y Yield", f"{tnx:.2f}%"],
        ["Gold", f"${gold:.2f}"],
        ["Bitcoin", f"${btc:.2f}"]
    ]
    df = pd.DataFrame(data, columns=["Asset", "Price/Level"])
    st.dataframe(df, use_container_width=True, hide_index=True)
