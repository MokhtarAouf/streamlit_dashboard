import streamlit as st
from PIL import Image
import folium
from streamlit_folium import st_folium

def show_home():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .big-font {
            font-size: 2.5rem;
            font-weight: bold;
            color: #2C3E50;
            margin-bottom: 0.5rem;
        }
        .subtitle-font {
            font-size: 1.5rem;
            color: #34495E;
            margin-bottom: 1rem;
        }
        .section-font {
            font-size: 2rem;
            font-weight: bold;
            color: #2C3E50;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        .text-font {
            font-size: 1.2rem;
            color: #34495E;
            line-height: 1.6;
            margin-bottom: 1.5rem;
        }
        .decorative-line {
            height: 3px;
            background: #3498DB;
            margin: 20px 0;
        }
        .map-container {
            border: 2px solid #3498DB;
            border-radius: 10px;
            padding: 10px;
            background-color: #ECF0F1;
        }
        .map-legend {
            background-color: #ECF0F1;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
        }
        .framed-image {
            border: 5px solid #3498DB;  /* Frame color */
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  /* Subtle shadow for aesthetics */
            margin-bottom: 10px;
            display: block;  /* Ensure it's treated as a block element */
            margin-left: auto; /* Align to the center */
            margin-right: auto; /* Align to the center */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main content
    col1, col2 = st.columns([1, 1])

    with col1:
        img_path = 'static/images/photo2.jpg'
        img = Image.open(img_path)
        st.markdown('<div class="framed-image">', unsafe_allow_html=True)
        st.image(img, width=200)  # Adjust width as needed
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("<h1 class='big-font'>Hi, I'm Mokhtar Aouf</h1>", unsafe_allow_html=True)
        st.markdown("<p class='subtitle-font'>Student in Data Engineering at EFREI Paris</p>", unsafe_allow_html=True)

    st.markdown("<div class='decorative-line'></div>", unsafe_allow_html=True)

    st.markdown("<h2 class='section-font'>Welcome to my Portfolio!</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p class='text-font'>Currently in my fourth year of Engineering at EFREI Paris. I major in Data Science and this portfolio showcases my journey and achievements.</p>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='decorative-line'></div>", unsafe_allow_html=True)

    # Map section
    st.markdown("<h3 class='section-font'>My Life on a Map 🌍</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<div class='map-container'>", unsafe_allow_html=True)
        home = [48.837589, 2.30106]
        internship = [48.827806, 2.264122]
        school = [48.7889, 2.3638]
        center_lat = (home[0] + internship[0] + school[0]) / 3
        center_lon = (home[1] + internship[1] + school[1]) / 3
        center = [center_lat, center_lon]
        m = folium.Map(location=center, zoom_start=12, tiles='cartodbpositron')

        def create_emoji_icon(emoji):
            return folium.CustomIcon(
                icon_image=f'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y=".9em" font-size="90">{emoji}</text></svg>',
                icon_size=(30, 30),
                icon_anchor=(15, 15),
            )

        folium.Marker(location=home, icon=create_emoji_icon('🏠')).add_to(m)
        folium.Marker(location=internship, icon=create_emoji_icon('💼')).add_to(m)
        folium.Marker(location=school, icon=create_emoji_icon('🏛️')).add_to(m)
        st_folium(m, height=300)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div class='map-legend'>
            <h4 style='color: #2C3E50;'>Map Legend</h4>
            <p>🏠 - Home</p>
            <p>💼 - Internship Location</p>
            <p>🏛️ - School: EFREI Paris</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div class='decorative-line'></div>", unsafe_allow_html=True)

    # Call to action
    st.markdown("<h3 class='section-font'>Explore My Journey</h3>", unsafe_allow_html=True)
    st.markdown(
        "<p class='text-font'>Feel free to navigate through the different sections of my portfolio to learn more about my projects, skills, and experiences.</p>",
        unsafe_allow_html=True
    )

def main():
    show_home()

if __name__ == "__main__":
    main()
