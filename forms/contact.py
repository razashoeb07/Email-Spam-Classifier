import streamlit as st
import re

def is_valid_email(email):
    # Basic email pattern validation
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def contact_form(key):
    with st.form(f"contact_form_{key}"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not name.strip():
                st.error("❌ Please enter your name.")
            elif not email.strip():
                st.error("❌ Please enter your email address.")
            elif not is_valid_email(email):
                st.error("❌ Please enter a valid email address (e.g., example@gmail.com).")
            elif not message.strip():
                st.error("❌ Please enter your message.")
            else:
                st.success("✅ Message successfully sent!")

