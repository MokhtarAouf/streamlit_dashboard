import streamlit as st

def portfolio_navbar():
    """Portfolio navigation to select between pages."""
    return st.sidebar.selectbox(
        "Portfolio Navigation",
        ['Home', 'Projects','About Me','Experience','Contact']
    )
