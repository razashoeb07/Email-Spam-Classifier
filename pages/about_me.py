import streamlit as st
import base64
from forms.contact import contact_form  # Make sure this file exists

# --- Contact Form Visibility Flags ---
if "show_contact_form" not in st.session_state:
    st.session_state.show_contact_form = {
        "contact_shoeb": False,
        "contact_saif": False
    }

# --- Function to Encode Image to Base64 ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- Function to Render Profile ---
def render_profile(name, bio, image_path, resume_path, contact_key, resume_key,
                   experience_text, skills_text, linkedin_url=None):
    col1, col2 = st.columns([1, 2], gap="medium")

    with col1:
        image_base64 = get_base64_image(image_path)
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center; height: 240px;">
                <img src="data:image/jpeg;base64,{image_base64}"
                style="border-radius: 50%; width: 230px; height: 230px; object-fit: cover; border: 4px solid #ff4b4b;"/>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(f"<h1 style='margin-bottom: 0;'>{name}</h1>", unsafe_allow_html=True)
        st.write(bio)

        button_col1, button_col2, button_col3 = st.columns(3, gap="small")

        with button_col1:
            if st.button("Contact Me", key=f"btn_{contact_key}"):
                st.session_state.show_contact_form[contact_key] = not st.session_state.show_contact_form[contact_key]

        with button_col2:
            with open(resume_path, "rb") as pdf_file:
                resume_data = pdf_file.read()
            st.download_button(
                label="Resume ",
                data=resume_data,
                file_name=f"{name.replace(' ', '_')}_Resume.pdf",
                mime="application/pdf",
                key=resume_key,
            )

        with button_col3:
            if linkedin_url:
                st.markdown(
                    """
                    <style>
                    .linkedin-button {
                        text-decoration: none;
                        font-size: 16px;
                        padding: 7px 15px;
                        border: 1px solid #0A66C2;
                        border-radius: 5px;
                        color: #0A66C2;
                        display: inline-flex;
                        align-items: center;
                        gap: 6px;
                        font-weight: 600;
                        transition: background-color 0.3s ease, color 0.3s ease;
                        position: relative;
                        top: -18px;
                    }
                    .linkedin-button:hover {
                        background-color: #0A66C2;
                        color: white !important;
                        text-decoration: none;
                    }
                    .linkedin-button img {
                        filter: invert(0%);
                        transition: filter 0.3s ease;
                    }
                    .linkedin-button:hover img {
                        filter: invert(100%);
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f"""
                    <a href="{linkedin_url}" target="_blank" class="linkedin-button">
                        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="20" height="20" alt="LinkedIn Icon" />
                        LinkedIn
                    </a>
                    """,
                    unsafe_allow_html=True,
                )

        if st.session_state.show_contact_form.get(contact_key):
            st.markdown("Contact Form")
            contact_form(contact_key)

    st.write("\n")
    st.subheader("Experience & Qualifications", anchor=False)
    st.write(experience_text)

    st.write("\n")
    st.subheader("Technical Skills", anchor=False)
    st.write(skills_text)
    st.markdown("---")

# --- PROFILE 1: Shoeb Raza ---
shoeb_experience = """
- Completed MCA with a strong foundation in programming and data analysis
- Hands-on experience with Python, SQL, and data visualization tools
- Developed multiple projects, including major data analysis and ML projects
- Strong understanding of data structures, algorithms, and core CS concepts
- Quick learner with excellent problem-solving skills and teamwork abilities
"""

shoeb_skills = """
- Data Structures & Algorithms (DSA)
- Programming Languages: Python, C, C++, Java
- Data Analysis Tools: Pandas, NumPy, Matplotlib
- Data Visualization: Matplotlib, Seaborn
- Web Development: HTML5, CSS, Django
- Database Management: MySQL, PostgreSQL
- Machine Learning: Supervised Learning, Classification, and Regression
"""

# --- PROFILE 2: Md Saif Khan ---
saif_experience = """
- Completed MCA in Computer Science with internships focused on MERN stack development
- Developed multiple full-stack web applications using MongoDB, Express.js, React.js, and Node.js
- Designed and implemented RESTful APIs and integrated frontend with backend services
- Worked in agile teams, collaborating closely with designers and QA to deliver client-ready solutions
"""

saif_skills = """
- Programming Languages: JavaScript (ES6+), C++, Java
- Frontend: React.js, HTML5, CSS3, Bootstrap
- Backend: Node.js, Express.js
- Database: MongoDB, PostgreSQL, MySQL
- Tools & Others: Git, Docker, Postman
"""

# --- Render both profiles ---
render_profile(
    name="Shoeb Raza",
    bio="Enthusiastic Python Developer with a passion for building efficient and scalable solutions. Eager to apply programming skills to real-world challenges.",
    image_path="./assets/raza.jpg",
    resume_path="./assets/Shoebraza_Python_Developer_25(1) (1).pdf",
    contact_key="contact_shoeb",
    resume_key="resume_shoeb",
    experience_text=shoeb_experience,
    skills_text=shoeb_skills,
    linkedin_url="https://www.linkedin.com/in/shoebraza02"
)

render_profile(
    name="Md Saif Khan",
    bio="Full-Stack Developer with experience in building responsive web applications and scalable backends. Passionate about tech and learning.",
    image_path="./assets/saif.jpeg",
    resume_path="./assets/resume_saif.pdf",
    contact_key="contact_saif",
    resume_key="resume_saif",
    experience_text=saif_experience,
    skills_text=saif_skills,
    linkedin_url="http://linkedin.com/in/md-saif-khan-186849223"
)