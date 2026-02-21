import streamlit as st
from api.news import get_top_news
from utils.time import get_pst_time

def execute_sentiment():
    st.header("MACRO SENTIMENT ANALYSIS")
    st.caption(get_pst_time())
    
    with st.spinner("Fetching macro news..."):
        try:
            articles = get_top_news("global macro markets")
            if not articles:
                st.warning("No news articles found.")
                return
                
            for i, a in enumerate(articles[:5], 1):
                st.markdown(f"**{i}. {a.get('title')}**")
                st.caption(f"{a.get('source', {}).get('name')} - {a.get('publishedAt')}")
                st.divider()
        except Exception as e:
            st.error(f"Error fetching sentiment: {e}")
