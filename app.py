import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# ---------------- CONFIG -----------------
st.set_page_config(page_title="Portfolio | Ojas", page_icon="💼", layout="wide")

# ----------- CUSTOM CSS ------------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #f7f8f8, #acbb78);
    }
    .big-font {
        font-size:42px !important;
        font-weight: bold;
        color: #2c3e50;
    }
    .subtitle {
        font-size:20px !important;
        color: #2c3e50;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.15);
        margin-bottom: 20px;
    }
    .social a {
        text-decoration: none;
        margin-right: 15px;
        font-size: 22px;
    }
    </style>
""", unsafe_allow_html=True)


# ----------------- SIDEBAR NAV ------------------
with st.sidebar:
    selected = option_menu(
        menu_title="Navigate",
        options=["🏠 Home", "👨 About", "🛠 Skills", "📂 Projects", "📄 Resume", "✉️ Contact"],
        icons=["house", "person", "tools", "code-slash", "file-earmark-text", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# ---------------- HOME ------------------
if selected == "🏠 Home":
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown('<p class="big-font">Hi, I am <span style="color:#16a085">Ojas</span> 👋</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Data Scientist | ML Engineer | AI Enthusiast</p>', unsafe_allow_html=True)
        st.write(
            "🚀 Passionate about AI, NLP, Agentic AI, and Cloud (AWS). "
            "I build intelligent systems that solve real-world problems."
        )
        st.write("🌱 Currently learning AWS Solutions Architect & building AI-powered apps.")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=220)

# ---------------- ABOUT ------------------
elif selected == "👨 About":
    st.markdown('<p class="big-font">About Me</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="card">
        I am a BSc Data Science student, building projects in AI/ML, NLP, and Cloud.  
        My goal is to combine intelligent agents with business solutions.  

        🔹 Interests: NLP, Agentic AI, AWS, and Full-Stack ML Apps  
        🔹 Strengths: Problem-Solving, Creativity, Communication  
        🔹 Future Vision: To launch an AI startup 🚀  
        </div>
        """, unsafe_allow_html=True)

# ---------------- SKILLS ------------------
elif selected == "🛠 Skills":
    st.markdown('<p class="big-font">My Skills</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card">📊 <b>Data Science</b><br>Python, Pandas, Numpy, Scikit-learn</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card">🤖 <b>Machine Learning</b><br>Regression, NLP, Recommendation Systems</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card">☁️ <b>Cloud & Tools</b><br>AWS, Docker, Git, Streamlit</div>', unsafe_allow_html=True)

# ---------------- PROJECTS ------------------
elif selected == "📂 Projects":
    st.markdown('<p class="big-font">Projects</p>', unsafe_allow_html=True)

    st.markdown('<div class="card">📌 <b>BuyBuddy</b> - Conversational Shopping Agent (n8n + Payman)</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📌 <b>BillBuddy</b> - Smart Bill Analyzer (Streamlit + Gemini)</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📌 <b>Secure File Upload Portal</b> - AWS EC2, S3, IAM, VPC</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📌 <b>AI Research Agent</b> - AutoGen, LangChain, Arxiv</div>', unsafe_allow_html=True)

# ---------------- RESUME ------------------
elif selected == "📄 Resume":
    st.markdown('<p class="big-font">My Resume</p>', unsafe_allow_html=True)

    with open("resume.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📥 Download Resume",
        data=PDFbyte,
        file_name="Ojas_Resume.pdf",
        mime="application/pdf",
    )

    st.markdown('<div class="card">You can download my latest resume above 👆</div>', unsafe_allow_html=True)

# ---------------- CONTACT ------------------
elif selected == "✉️ Contact":
    st.markdown('<p class="big-font">Get in Touch</p>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">
        📧 Email: <a href="mailto:ojas@example.com">ojas@example.com</a><br>
        💼 LinkedIn: <a href="https://linkedin.com">linkedin.com/in/ojas</a><br>
        🐙 GitHub: <a href="https://github.com">github.com/ojas</a><br>
        📱 Instagram: <a href="https://instagram.com">instagram.com/ojas</a><br>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<p class="subtitle">🤝 Let’s collaborate and build something amazing!</p>', unsafe_allow_html=True)
