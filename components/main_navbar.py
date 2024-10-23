import streamlit as st

def main_navbar():
    """Main navigation bar to switch between main sections."""
    
    st.sidebar.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .sidebar-nav {
        padding: 20px;
    }
    .sidebar-nav h2 {
        color: #2e7bcf;
        padding-bottom: 20px;
        border-bottom: 2px solid #e6e6e6;
        text-align: left;
        font-size: 24px;
        font-weight: bold;
    }
    .stSelectbox > div > div {
        background-color: white;
        color: #2e7bcf;
    }
    .stSelectbox [data-baseweb="select"] {
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown('<div class="sidebar-nav">', unsafe_allow_html=True)
    st.sidebar.markdown('<h2>Navigation</h2>', unsafe_allow_html=True)

    options = {
        'Portfolio': '📁 Portfolio',
        'Dataset Analysis': '📊 Dataset Analysis'
    }

    selected = st.sidebar.selectbox(
        "",
        options.keys(),
        format_func=lambda x: options[x],
        key="main_nav"
    )

    st.sidebar.markdown('</div>', unsafe_allow_html=True)

    return selected

# Example usage
if __name__ == "__main__":
    section = main_navbar()
    st.write(f"You selected: {section}")
