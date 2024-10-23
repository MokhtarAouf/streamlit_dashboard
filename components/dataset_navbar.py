import streamlit as st

def dataset_navbar():
    """Dataset Analysis navigation to select between pages."""
    return st.sidebar.selectbox(
        "Dataset Analysis Pages",
        ['Overview', 'Insights']
    )
