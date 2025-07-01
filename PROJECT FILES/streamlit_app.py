import streamlit as st
import requests

st.set_page_config(page_title="Smart City Assistant", layout="wide")
st.title("🌆 Sustainable Smart City Assistant")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧠 Ask Assistant", "📊 Forecast", "🚨 Anomaly Detection", "🌿 Eco Tips", "📄 Generate Report"])

# ----------------- TAB 1: Ask Assistant -----------------
with tab1:
    st.header("🧠 Ask Any Question")
    prompt1 = st.text_input("Enter your question:")
    if st.button("Ask", key="ask"):
        if prompt1:
            res = requests.post("http://127.0.0.1:8000/ask", json={"prompt": prompt1})
            st.success(res.json()["response"])
        else:
            st.warning("Please enter a question.")

# ----------------- TAB 2: Forecast -----------------
with tab2:
    st.header("📊 Forecast KPI")
    prompt2 = st.text_input("Enter forecasting topic:")
    if st.button("Forecast", key="forecast"):
        if prompt2:
            res = requests.post("http://127.0.0.1:8000/forecast", json={"prompt": prompt2})
            st.success(res.json()["forecast"])
        else:
            st.warning("Please enter a topic.")

# ----------------- TAB 3: Anomaly Detection -----------------
with tab3:
    st.header("🚨 Detect Anomalies")
    prompt3 = st.text_input("Enter data or topic:")
    if st.button("Detect", key="anomaly"):
        if prompt3:
            res = requests.post("http://127.0.0.1:8000/anomalies", json={"prompt": prompt3})
            st.success(res.json()["result"])
        else:
            st.warning("Please enter a value.")

# ----------------- TAB 4: Eco Tips -----------------
with tab4:
    st.header("🌿 Eco-Friendly Tips")
    prompt4 = st.text_input("Enter area (e.g., Water, Energy, Transportation):")
    if st.button("Get Tips", key="eco"):
        if prompt4:
            res = requests.post("http://127.0.0.1:8000/eco-tips", json={"prompt": prompt4})
            st.success(res.json()["tips"])
        else:
            st.warning("Please enter an area.")

# ----------------- TAB 5: Generate Sustainability Report -----------------
with tab5:
    st.header("📄 Generate Sustainability Report")
    prompt5 = st.text_area("Enter report topic:")
    if st.button("Generate Report", key="report"):
        if prompt5:
            res = requests.post("http://127.0.0.1:8000/generate-report", json={"prompt": prompt5})
            st.success(res.json()["report"])
        else:
            st.warning("Please enter a topic.")
