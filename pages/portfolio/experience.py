import streamlit as st
from PIL import Image
import os

def load_image(image_file, max_width=300):
    if os.path.exists(image_file):
        img = Image.open(image_file)
        width, height = img.size
        if width > max_width:
            ratio = max_width / width
            new_size = (max_width, int(height * ratio))
            img = img.resize(new_size)
        return img
    return None

def show_experience():
    st.markdown("""
    <style>
    .big-font {
        font-size: 44px !important;  /* Increased font size for the main title */
        font-weight: bold;
        color: #1E90FF;
        margin-bottom: 20px;
    }
    .medium-font {
        font-size: 38px !important;  /* Increased font size for job titles */
        color: #4682B4;
        margin-bottom: 10px;
    }
    .experience-text {
        font-size: 30px !important;  /* Further increased font size for descriptions */
        background-color: #E6F3FF;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #1E90FF;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .experience-text ul {
        padding-left: 20px;
    }
    .experience-text li {
        margin-bottom: 15px;
    }
    .framed-image {
        border: 5px solid #1E90FF;  /* Adds a frame around the image */
        border-radius: 10px;
        overflow: hidden;  /* Ensures rounded corners are applied to the image */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Professional Experience</p>', unsafe_allow_html=True)

    # Sardé Experience
    st.markdown('<p class="medium-font">Waiter at Sardé Restaurant</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">July 2024 - Present</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([0.6, 2.4])  # Adjusted the column ratio to give more space to the text
    with col1:
        image = load_image("assets/images/photo3.jpg")
        if image:
            st.markdown('<div class="framed-image">', unsafe_allow_html=True)
            st.image(image, caption="Sardé Restaurant", use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.write("Image not available")

    with col2:
        st.markdown("""
        <div class="experience-text">
        <ul>
        <li><strong>Warmly welcomed customers</strong> and presented the concept of modern Lebanese cuisine.</li>
        <li><strong>Explained the menu and dishes in detail</strong>, engaging in conversations to enhance customer experience.</li>
        <li><strong>Maintained cleanliness and organization</strong> in the restaurant and managed dishware efficiently.</li>
        <li><strong>Demonstrated punctuality and professionalism</strong> in all daily tasks and interactions.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # Add space between experiences

    # City One Experience
    st.markdown('<p class="medium-font">City One - Olympic Games Orientation Agent</p>', unsafe_allow_html=True)
    st.markdown('<p class="medium-font">July 2024 - September 2024</p>', unsafe_allow_html=True)

    col1, col2 = st.columns([0.6, 2.4])
    with col1:
        image = load_image("assets/images/photo4.jpg")
        if image:
            image = image.transpose(Image.ROTATE_270)
            st.markdown('<div class="framed-image">', unsafe_allow_html=True)
            st.image(image, caption="Olympic Games Orientation", use_column_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.write("Image not available")

    with col2:
        st.markdown("""
        <div class="experience-text">
        <ul>
        <li><strong>Controlled traffic</strong> in an Olympic lane, ensuring only authorized vehicles passed through.</li>
        <li><strong>Distributed parking tickets</strong> and guided visitors to appropriate parking areas.</li>
        <li><strong>Communicated professionally</strong> with tourists and locals, providing assistance and information.</li>
        <li><strong>Guided and informed visitors</strong> about routes and ongoing construction work affecting transportation.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_experience()
