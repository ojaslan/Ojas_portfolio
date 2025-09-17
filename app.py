import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# ---------------- CONFIG -----------------
st.set_page_config(page_title="Portfolio | Ojas", page_icon="💼", layout="wide")

# ----------- CUSTOM CSS ------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #f7f8f8, #acbb78);
    }
    .big-font {
        font-size:42px !important;
        font-weight: bold;
    }
    .subtitle {
        font-size:20px !important;
        color: #555;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
        margin-bottom: 15px;
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
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=220)

# ---------------- ABOUT -------------------
elif selected == "About":
    st.markdown(
        """
        <div class="card">
        I am a BSc Data Science student, building projects in AI/ML, NLP, and Generative AI.  
        My goal is to combine intelligent autonomous agents with real-world business solutions.  

        🔹 Interests: NLP, Agentic AI, AutoGen, and GenAI Applications  
        🔹 Strengths: Problem-Solving, Creativity, Communication  
        🔹 Future Vision: To launch an AI startup 🚀  
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------- SKILLS ------------------
elif selected == "Skills":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="card">📊 <b>Data Science</b><br>Python, Pandas, Numpy, Scikit-learn</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card">🤖 <b>Machine Learning & NLP</b><br>Regression, NLP, Recommendation Systems</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="card">🧠 <b>Agentic AI & GenAI Tools</b><br>AutoGen, LangChain, Streamlit</div>', unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif selected == "Projects":
    st.markdown('<div class="card">📌 <b>BuyBuddy</b> - Conversational Shopping Agent (n8n + Payman)</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📌 <b>BillBuddy</b> - Smart Bill Analyzer (Streamlit + Gemini)</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📌 <b>AI Research Agent</b> - AutoGen, LangChain, Arxiv</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📌 <b>Agentic Workflows</b> - Building autonomous AI systems with AutoGen</div>', unsafe_allow_html=True)

# ---------------- CONTACT -----------------
elif selected == "Contact":
    st.markdown(
        """
        <div class="card">
        📧 Email: <a href="mailto:ojas@example.com">ojas@example.com</a><br>
        💼 LinkedIn: <a href="https://www.linkedin.com">linkedin.com/in/ojas</a><br>
        🐙 GitHub: <a href="https://github.com">github.com/ojas</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
