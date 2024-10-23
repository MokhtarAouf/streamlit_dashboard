import streamlit as st

def portfolio_navbar():
    """Displays the portfolio navigation menu."""
    return st.sidebar.selectbox(
        "Choose your page",
        ["Home", "About Me", "Projects", "Contact"]
    )
