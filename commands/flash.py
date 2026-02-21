import streamlit as st
from api.yahoo import get_price_history
from utils.time import get_pst_time

def execute_flash(ticker: str):
    st.header(f"FLASH ANALYSIS: {ticker.upper()}")
    st.caption(get_pst_time())
    
    with st.spinner(f"Fetching data for {ticker}..."):
        df = get_price_history(ticker, period="1mo", interval="1d")
        if df.empty:
            st.warning(f"No data found for {ticker}")
            return
            
        start_price = df['Close'].iloc[0]
        end_price = df['Close'].iloc[-1]
        change = ((end_price - start_price) / start_price) * 100
        
        st.metric(
            label=f"{ticker.upper()} Current Price", 
            value=f"${end_price:.2f}", 
            delta=f"{change:.2f}% (30-Day)"
        )
        
        st.line_chart(df['Close'])
