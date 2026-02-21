import streamlit as st
import sys

def handle_api_error(api_name: str, message: str):
    st.error(f"API Error: {api_name}\n\n{message}")

def handle_missing_key(api_name: str, env_var: str):
    st.warning(f"Missing API Key: The {api_name} API requires the environment variable '{env_var}' to be set.")
    st.stop()
