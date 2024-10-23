import streamlit as st
from components.main_navbar import main_navbar
from components.portfolio_navbar import portfolio_navbar
from pages.portfolio import home, about, projects, experience, contact
from pages.dataset_analysis import overview, insights

def main():
    st.set_page_config(page_title="Portfolio & Data Analysis Dashboard", layout="wide")
    
    main_section = main_navbar()

    if main_section == "Portfolio":
        portfolio_section = portfolio_navbar()
        
        if portfolio_section == "Home":
            home.show_home()
        elif portfolio_section == "About Me":
            about.show_about()
        elif portfolio_section == "Projects":
            projects.show_projects()
        elif portfolio_section == "Experience":
            experience.show_experience()
        elif portfolio_section == "Contact":
            contact.show_contact()
    
    elif main_section == "Dataset Analysis":
        analysis_type = st.sidebar.radio("Choose analysis type", ["Overview", "Insights"])
        if analysis_type == "Overview":
            overview.show_overview()
        else:
            insights.show_insights()

if __name__ == "__main__":
    main()
