import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import importlib

# Import the contact module relatively
contact_module = importlib.import_module('.contact', package='pages.portfolio')

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def show_projects():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .project-title {
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 2rem;
            color: #1E88E5;
            text-align: center;
            text-shadow: 2px 2px 4px #87CEFA;
        }
        .project-section {
            font-size: 1.1rem;
            margin-bottom: 1rem;
            background-color: #E6F3FF;
            padding: 1rem;
            border-radius: 10px;
            border-left: 5px solid #1E88E5;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .tech-badge {
            display: inline-block;
            padding: 0.3rem 0.5rem;
            margin: 0.2rem;
            background-color: #4CAF50;
            color: white;
            border-radius: 15px;
            font-size: 0.9rem;
            font-weight: bold;
        }
        .section-header {
            color: #1E88E5;
            border-bottom: 2px solid #1E88E5;
            padding-bottom: 10px;
            margin-top: 30px;
            font-size: 1.8rem;
            font-weight: bold;
        }
        .decorative-line {
            height: 3px;
            background: linear-gradient(to right, #1E88E5, #87CEFA, #E6F3FF);
            margin: 20px 0;
        }
        .expander-header {
            font-size: 1.4rem;
            color: #1E88E5;
            font-weight: bold;
        }
        .stButton > button {
            display: block;
            margin: 0 auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title and Lottie animation
    st.markdown('<div class="project-title">My Projects</div>', unsafe_allow_html=True)
    lottie_coding = load_lottie_url('https://assets10.lottiefiles.com/packages/lf20_w51pcehl.json')
    st_lottie(lottie_coding, height=200, key="coding")

    # Decorative line
    st.markdown("<div class='decorative-line'></div>", unsafe_allow_html=True)

    # Project 1: Streamlit Dashboard
    with st.expander("🌟 Project 1: Streamlit Dashboard - Portfolio and Comorbidities Analysis", expanded=True):
        st.markdown("<h3 class='section-header'>Interactive Portfolio and Data Analysis Dashboard</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="project-section">
            Developed a comprehensive Streamlit dashboard showcasing my portfolio and conducting in-depth analysis of a comorbidities dataset.
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<strong>Key Features:</strong>", unsafe_allow_html=True)
        features = [
            "Built an interactive portfolio website using Streamlit and Python",
            "Conducted deep analysis on a comorbidities dataset to uncover insights and patterns",
            "Created visualizations to tell a compelling story from the data",
            "Implemented interactive elements for user engagement"
        ]
        for feature in features:
            st.markdown(f"- {feature}")
        
        st.markdown("<strong>Technologies Used:</strong>", unsafe_allow_html=True)
        st.markdown(
            """
            <span class="tech-badge">Python</span>
            <span class="tech-badge">Streamlit</span>
            <span class="tech-badge">Pandas</span>
            <span class="tech-badge">Matplotlib</span>
            <span class="tech-badge">Seaborn</span>
            """,
            unsafe_allow_html=True
        )

    # Project 2: Data Pipeline
    with st.expander("🚀 Project 2: Advanced Data Pipeline for Book Analysis", expanded=True):
        st.markdown("<h3 class='section-header'>Comprehensive Data Pipeline for Book Data Analysis</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="project-section">
            Designed and implemented a robust data pipeline to collect, process, and analyze book data from multiple sources.
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<strong>Pipeline Components:</strong>", unsafe_allow_html=True)
            components = [
                "Data Collection: Scraped book data using two different APIs",
                "Data Ingestion: Utilized Apache Kafka for real-time data streaming",
                "Data Processing: Leveraged PySpark for distributed data processing",
                "Data Storage: Implemented Hadoop Distributed File System (HDFS)",
                "Containerization: Dockerized the entire pipeline for easy deployment"
            ]
            for component in components:
                st.markdown(f"- {component}")
        
        with col2:
            st.markdown("<strong>Key Achievements:</strong>", unsafe_allow_html=True)
            achievements = [
                "Processed and analyzed over 1 million book records",
                "Implemented real-time data streaming with latency under 100ms",
                "Achieved 99.9% uptime for the entire pipeline",
                "Reduced data processing time by 70% compared to traditional methods"
            ]
            for achievement in achievements:
                st.markdown(f"- {achievement}")

        st.markdown("<strong>Technologies Used:</strong>", unsafe_allow_html=True)
        st.markdown(
            """
            <span class="tech-badge">Python</span>
            <span class="tech-badge">Docker</span>
            <span class="tech-badge">Apache Kafka</span>
            <span class="tech-badge">PySpark</span>
            <span class="tech-badge">Hadoop</span>
            <span class="tech-badge">API Integration</span>
            """,
            unsafe_allow_html=True
        )

    # Project 3: Patent Classification System
    with st.expander("🧠 Project 3: Patent Classification System", expanded=True):
        st.markdown("<h3 class='section-header'>Explainable Patent Learning for Artificial Intelligence Modeling</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="project-section">
            Development of an AI-based patent classification model with high performance (F1 score above 0.85), 
            including explanation methods such as LIME and SHAP.
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<strong>Key Features:</strong>", unsafe_allow_html=True)
        features = [
            "Developed a high-performance patent classification model",
            "Implemented explainable AI techniques (LIME and SHAP)",
            "Optimized for inference time under 60 seconds",
            "Managed large-scale patent data using PostgreSQL and Elasticsearch"
        ]
        for feature in features:
            st.markdown(f"- {feature}")

        st.markdown("<strong>Technologies Used:</strong>", unsafe_allow_html=True)
        st.markdown(
            """
            <span class="tech-badge">Python</span>
            <span class="tech-badge">TensorFlow</span>
            <span class="tech-badge">PyTorch</span>
            <span class="tech-badge">Scikit-learn</span>
            <span class="tech-badge">PostgreSQL</span>
            <span class="tech-badge">Elasticsearch</span>
            """,
            unsafe_allow_html=True
        )

    # Project 4: Data Analysis
    with st.expander("📊 Project 4: Data Analysis", expanded=True):
        st.markdown("<h3 class='section-header'>Comprehensive Data Analysis Project</h3>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="project-section">
            Conducted an end-to-end data analysis project, from data preparation to machine learning modeling.
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<strong>Project Phases:</strong>", unsafe_allow_html=True)
            phases = [
                "Data Preparation: Merged records, selected and calculated new attributes, cleaned data",
                "Exploratory Data Analysis (EDA): Identified target variables, used statistical visualizations",
                "Machine Learning Modeling:",
                "  - Unsupervised Learning: Applied clustering techniques",
                "  - Supervised Learning: Developed predictive models for real estate prices"
            ]
            for phase in phases:
                st.markdown(f"- {phase}")

        with col2:
            st.markdown("<strong>Key Achievements:</strong>", unsafe_allow_html=True)
            achievements = [
                "Successfully cleaned and prepared a complex dataset for analysis",
                "Uncovered key insights through thorough exploratory data analysis",
                "Developed a predictive model with high accuracy for real estate price prediction",
                "Applied clustering techniques to discover natural groupings in the data"
            ]
            for achievement in achievements:
                st.markdown(f"- {achievement}")

        st.markdown("<strong>Technologies Used:</strong>", unsafe_allow_html=True)
        st.markdown(
            """
            <span class="tech-badge">Python</span>
            <span class="tech-badge">Pandas</span>
            <span class="tech-badge">NumPy</span>
            <span class="tech-badge">Scikit-learn</span>
            <span class="tech-badge">Matplotlib</span>
            <span class="tech-badge">Seaborn</span>
            """,
            unsafe_allow_html=True
        )

    # Decorative line
    st.markdown("<div class='decorative-line'></div>", unsafe_allow_html=True)

    # Add a section for user to get in touch or learn more
    st.markdown("<h3 class='section-header'>Want to learn more about my projects?</h3>", unsafe_allow_html=True)
    
    if st.button("Contact Me", key="contact_button"):
        # Instead of using st.switch_page, we'll call the show_contact function directly
        if hasattr(contact_module, 'show_contact'):
            contact_module.show_contact()
        else:
            st.error("Contact page function not found. Please check the contact.py file.")

# Make sure this function is called in your main app file
# Don't forget to install streamlit-lottie: pip install streamlit-lottie

if __name__ == "__main__":
    show_projects()
