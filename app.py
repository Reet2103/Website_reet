import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Reet Bhardwaj - Resume", layout="wide")

# Load image
image = Image.open("assets/reet_photo.jpg")

# Custom CSS for dark/light mode and animations
st.markdown("""
<style>
    /* Dark/Light Mode Toggle */
    .stApp {
        transition: background-color 0.3s, color 0.3s;
    }
    .dark-mode {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .dark-mode .stButton button {
        background-color: #333;
        color: #fff;
    }

    /* Hero Section Animation */
    @keyframes slideIn {
        from { transform: translateX(-100%); }
        to { transform: translateX(0); }
    }
    .hero {
        display: flex;
        align-items: center;
        animation: slideIn 1.5s ease-out;
    }

    /* Ladder Format for Education */
    .education-timeline {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-left: 20px;
    }
    .education-timeline div {
        margin-bottom: 20px;
        position: relative;
    }
    .education-timeline div::before {
        content: '';
        position: absolute;
        left: -20px;
        top: 0;
        width: 10px;
        height: 100%;
        background: #ccc;
    }

    /* Horizontal Sliding Certifications */
    .certifications-carousel {
        display: flex;
        overflow-x: auto;
        gap: 20px;
        padding: 10px;
    }
    .certification-card {
        min-width: 200px;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Dark/Light Mode Toggle
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Add toggle button to the sidebar
with st.sidebar:
    st.button("🌙 Toggle Dark Mode", on_click=toggle_dark_mode)

# Apply dark/light mode
if st.session_state.dark_mode:
    st.markdown('<div class="dark-mode">', unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.image(image, width=200)
with col2:
    st.title("Reet Bhardwaj")
    st.write("**Contact:** (+91) - 9389044023")
    st.write("**Email:** reebhardwaj2103@gmail.com")
    st.write("**LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/rect-bhardwaj-906642249/)")
    st.write("**GitHub:** [GitHub Profile](https://github.com/Reet2103)")
st.markdown('</div>', unsafe_allow_html=True)

# About Section
st.header("About Me")
st.write("An enthusiastic and highly motivated student with programming and analytical skills. I am actively seeking opportunities to expand my knowledge in the data analytics and data science domains. Known for my honesty, hard work, and flexibility, I enjoy taking initiatives and seeking out new challenges to further my growth and development.")

# Experience Section
st.header("Experience")
st.subheader("Zenylities, Data Analyst Intern (2nd Feb - 15 July 2024)")
st.write("""
- Worked as an Intern and learned Power BI and SQL.
- Performed data loading, cleaning, and visualization using Power BI.
- Created dashboards with DAX.
""")

st.subheader("Tata Forage, Virtual Internship")
st.write("""
- Strengthened Power BI skills and analyzed HR data for gender-related KPIs.
- Delivered actionable insights based on data analysis.
""")

# Education Section
st.header("Education")
st.markdown("""
<div class="education-timeline">
    <div><strong>University of Delhi, Delhi</strong> - Graduation (2021-24)</div>
    <div><strong>Renaissance School, Bulandshahr(U.P.)</strong> - 12th (2021)</div>
    <div><strong>Nirmala Convent School, Bulandshahr(U.P.)</strong> - 10th (2019)</div>
</div>
""", unsafe_allow_html=True)

# Skills Section
st.header("Skills")
st.write("""
- **Technical Skills:** Power BI, SQL, Python, MS Excel, ChatGPT.
- **Soft Skills:** Communication, adaptability, time management.
""")

# Projects Section
st.header("Projects")
st.subheader("Python - Tic Tac Toe Game")
st.write("""
- Designed for single-player and multiplayer modes.
- Managed game logic using Python.
""")

st.subheader("Power BI - Sales Data Analysis")
st.write("""
- Analyzed retail sales data and created interactive dashboards.
- Visualized sales trends and identified top-performing products.
""")

st.subheader("Power BI - Customer Satisfaction Dashboard")
st.write("""
- Designed a dashboard to monitor customer satisfaction scores.
- Integrated data from multiple sources and performed data cleaning.
""")

# Certifications Section
st.header("Certifications")
st.markdown("""
<div class="certifications-carousel">
    <div class="certification-card">Attended 7-day bootcamp on Python and AI by Devtown</div>
    <div class="certification-card">Internship certificate at Zenylities: Power BI and SQL</div>
    <div class="certification-card">Tata Forage Virtual Internship</div>
</div>
""", unsafe_allow_html=True)

# Close dark mode div
if st.session_state.dark_mode:
    st.markdown('</div>', unsafe_allow_html=True)