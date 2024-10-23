import streamlit as st

def show_contact():
    st.title("Contact Me")

    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        user_email = st.text_input("Your Email")
        message = st.text_area("Message")
        
        submit_button = st.form_submit_button("Send")
        
        if submit_button:
            # Instead of sending an email, we'll display the submitted information
            st.success(f"Message received! Thank you, {name}.")
            st.write("Message details:")
            st.write(f"From: {name} ({user_email})")
            st.write("Message:")
            st.write(message)
            
            # You could also add code here to save the message to a file or database
            # For example:
            # with open("messages.txt", "a") as f:
            #     f.write(f"From: {name} ({user_email})\nMessage: {message}\n\n")

    # Add some information about how you can be contacted
    st.markdown("---")
    st.write("You can also reach me at:")
    st.write("Email: mokhtar.aouf@gmail.com or mokhtar.aouf@efrei.net")
    st.write("LinkedIn: [www.linkedin.com/in/mokhtar-aouf-87a636222)")
    st.write("GitHub: [https://github.com/MokhtarAouf")
