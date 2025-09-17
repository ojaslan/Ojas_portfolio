import streamlit as st
from streamlit_option_menu import option_menu

# ---------------- CONFIG -----------------
st.set_page_config(page_title="Portfolio | Ojas", page_icon="💼", layout="wide")

# ----------- CUSTOM CSS ------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #f7f8f8, #acbb78);
        font-family: 'Segoe UI', sans-serif;
    }
    .big-font {
        font-size:42px !important;
        font-weight: bold;
        color: #2c3e50;
    }
    .subtitle {
        font-size:20px !important;
        color: #555;
        margin-bottom: 20px;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
        margin-bottom: 15px;
        font-size: 16px;
        line-height: 1.5;
    }
    .profile-pic {
        width:220px;
        height:220px;
        border-radius:50%;
        object-fit:cover;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------- SIDEBAR ----------------
with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Home", "About", "Skills", "Projects", "Contact"],
        icons=["house", "person", "tools", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# ---------------- HOME --------------------
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<p class="big-font">Hi, I am <span style="color:#16a085">Ojas</span> 👋</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Data Scientist | ML Engineer | AI Enthusiast</p>', unsafe_allow_html=True)
        st.write(
            "🚀 Passionate about Artificial Intelligence, with a special focus on NLP, Generative AI, and Agentic AI. "
            "I enjoy building intelligent systems that think, act, and collaborate like humans."
        )
        st.write(
            "💡 Currently exploring advanced Agentic workflows with **AutoGen**, crafting autonomous AI agents that can research, reason, and solve complex problems. "
            "From smart assistants to research-driven tools, I love turning bold ideas into reality."
        )
        st.write(
            "🌱 Always experimenting with GenAI to push boundaries and create applications that are not just reactive—but proactive and adaptive."
        )
    with col2:
        st.markdown(
            """
            <div style='display:flex; justify-content:center;'>
                <img src='WhatsApp Image 2025-02-27 at 17.44.00_ff3d19f2.jpg' class='profile-pic'>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- ABOUT -------------------
elif selected == "About":
    st.markdown(
        """
        <div class="card">
        I am a <b>BSc Data Science student</b>, building projects in AI/ML, NLP, and Generative AI.  
        My goal is to combine intelligent autonomous agents with real-world business solutions.  

        🔹 <b>Interests</b>: NLP, Agentic AI, AutoGen, and GenAI Applications  
        🔹 <b>Strengths</b>: Problem-Solving, Creativity, Communication  
        🔹 <b>Future Vision</b>: To launch an AI startup 🚀  
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------- SKILLS ------------------
elif selected == "Skills":
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="card">📊 <b>Data Science</b><br>Python, Pandas, Numpy, Scikit-learn</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card">🤖 <b>Machine Learning & NLP</b><br>Regression, NLP, Recommendation Systems</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card">🖥️ <b>Frontend</b><br>Streamlit</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="card">🧠 <b>Agentic AI & GenAI Tools</b><br>AutoGen, LangChain, n8n</div>', unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif selected == "Projects":
    st.markdown('<div class="card">📌 <b>MiniMart</b> - An e-commerce website where transactions occur using AI (Payman AI).</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📌 <b>ByteCal</b> - An AI agent that tells you how many calories are in your food.</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📌 <b>Blog Generator</b> - Upload your photo or text, and a complete blog is generated for you.</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📌 <b>FinSight AI</b> - A personal financial AI assistant that gives you smart financial advice.</div>', unsafe_allow_html=True)

# ---------------- CONTACT -----------------
elif selected == "Contact":
    st.markdown(
        """
        <div class="card">
        📧 <b>Email</b>: <a href="mailto:ojaslanjekar750@gmail.com">ojaslanjekar750@gmail.com</a><br>
        💼 <b>LinkedIn</b>: <a href="https://www.linkedin.com/in/ojas" target="_blank">linkedin.com/in/ojas</a><br>
        🐙 <b>GitHub</b>: <a href="https://github.com/ojas" target="_blank">github.com/ojas</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
