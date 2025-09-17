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
    "🚀 Passionate about Artificial Intelligence, with a special focus on NLP, Generative AI, and Agentic AI. "
    "I enjoy building intelligent systems that think, act, and collaborate like humans."
)
st.write(
    "💡 Currently exploring advanced Agentic workflows with **Autogen**, crafting autonomous AI agents that can research, reason, and solve complex problems. "
    "From smart assistants to research-driven tools, I love turning bold ideas into reality."
)
st.write(
    "🌱 Always experimenting with GenAI to push boundaries and create applications that are not just reactive—but proactive and adaptive."
)
with col2:
    st.image("data:image/jpeg;base64,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", width=220)

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
