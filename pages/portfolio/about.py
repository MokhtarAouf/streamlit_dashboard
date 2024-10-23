import streamlit as st
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

def show_about():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .big-font {
            font-size: 24px !important;
            font-weight: bold;
            color: #1E90FF;
            text-shadow: 1px 1px 2px #87CEFA;
        }
        .highlight {
            background-color: #E6F3FF;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            border-left: 5px solid #4682B4;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .section-header {
            color: #4682B4;
            border-bottom: 2px solid #4682B4;
            padding-bottom: 10px;
            margin-top: 30px;
        }
        .large-text {  /* New class for increasing text size, without bold */
            font-size: 28px !important;
            color: #000000;  /* Changed color to black */
            margin-bottom: 15px;
        }
        .skill-badge {
            display: inline-block;
            background-color: #87CEFA;
            color: #000080;
            padding: 5px 10px;
            margin: 5px;
            border-radius: 15px;
            font-weight: bold;
        }
        .interest-badge {
            display: inline-block;
            background-color: #98FB98;
            color: #006400;
            padding: 5px 10px;
            margin: 5px;
            border-radius: 15px;
            font-weight: bold;
        }
        .decorative-line {
            height: 3px;
            background: linear-gradient(to right, #4682B4, #87CEFA, #E6F3FF);
            margin: 20px 0;
        }
        .stButton > button {
            display: block;
            margin: 0 auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title with custom styling
    st.markdown("<h1 style='text-align: center; color: #4682B4; text-shadow: 2px 2px 4px #87CEFA;'>About Me</h1>", unsafe_allow_html=True)

    # Add a Lottie animation
    lottie_coding = load_lottie_url('https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json')
    st_lottie(lottie_coding, height=200, key="coding")

    # Decorative line
    st.markdown("<div class='decorative-line'></div>", unsafe_allow_html=True)

    # Introduction
    st.markdown("<p class='big-font'>Hello! I'm Mokhtar, a multicultural tech enthusiast with a passion for data science and innovation.</p>", unsafe_allow_html=True)

    # Background
    st.markdown("<h2 class='section-header'>My Journey</h2>", unsafe_allow_html=True)
    st.markdown("<p class='large-text'>My story begins in Riyadh, Saudi Arabia, where I was born to Syrian parents. This multicultural background has shaped my worldview and given me a unique perspective on life and technology.</p>", unsafe_allow_html=True)

    # Education
    st.markdown("<h2 class='section-header'>Education</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='highlight'>
        🎓 <strong>Early Education:</strong> French School of Riyadh<br>
        🎓 <strong>High School:</strong> Baccalauréat Degree<br>
        🎓 <strong>Current:</strong> Pursuing higher education in Data Engineering at EFREI in Paris
        </div>
        """,
        unsafe_allow_html=True
    )

    # Life Transition
    st.markdown("<h2 class='section-header'>The Big Move</h2>", unsafe_allow_html=True)
    st.markdown("<p class='large-text'>After obtaining my Baccalauréat, I took a leap of faith and moved to Paris. This transition marked one of the most significant chapters in my life. Living independently for the first time, I faced challenges like adapting to a new culture, colder weather, and a completely different environment.</p>", unsafe_allow_html=True)

    # Skills and Interests
    st.markdown("<h2 class='section-header'>Skills & Interests</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<strong>Technical Skills:</strong>", unsafe_allow_html=True)
        st.markdown(
            """
            <span class='skill-badge'>Python Programming</span>
            <span class='skill-badge'>Data Analysis</span>
            <span class='skill-badge'>Machine Learning</span>
            <span class='skill-badge'>Web Development</span>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown("<strong>Personal Interests:</strong>", unsafe_allow_html=True)
        st.markdown(
            """
            <span class='interest-badge'>Basketball (PUC D4)</span>
            <span class='interest-badge'>New Technologies</span>
            <span class='interest-badge'>Traveling</span>
            <span class='interest-badge'>Sports</span>
            """,
            unsafe_allow_html=True
        )

    # Decorative line
    st.markdown("<div class='decorative-line'></div>", unsafe_allow_html=True)

    # Future Goals
    st.markdown("<h2 class='section-header'>Looking Ahead</h2>", unsafe_allow_html=True)
    st.markdown("<p class='large-text'>As I continue my journey in tech and data science, I'm excited about the possibilities that lie ahead. My goal is to leverage my unique background and skills to make meaningful contributions to the field of data engineering and analytics, driving innovation and solving complex problems.</p>", unsafe_allow_html=True)

    # Call to Action
    st.markdown("---")
    st.markdown("<h3 style='color: #4682B4; text-align: center;'>Let's Connect!</h3>", unsafe_allow_html=True)
    st.markdown("<p class='large-text'>I'm always open to discussing new projects, creative ideas, or opportunities to be part of your visions.</p>", unsafe_allow_html=True)

    if st.button("Contact Me", key="contact_button"):
        # Instead of using st.switch_page, we'll call the show_contact function directly
        if hasattr(contact_module, 'show_contact'):
            contact_module.show_contact()
        else:
            st.error("Contact page function not found. Please check the contact.py file.")

if __name__ == "__main__":
    show_about()
