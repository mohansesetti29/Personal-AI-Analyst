from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import pandas as pd

from backend.tools.eda import run_eda
from backend.agent import generate_hypotheses, explain_result
from backend.tools.validate import validate_hypothesis

st.set_page_config(page_title="AnalystGPT", layout="wide")

st.title("📊 AnalystGPT – Personal AI Data Analyst")

# Initialize session state
if "hypotheses" not in st.session_state:
    st.session_state.hypotheses = None
if "selected_hypothesis" not in st.session_state:
    st.session_state.selected_hypothesis = None

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    eda = run_eda(df)
    st.subheader("🔍 Dataset Summary")
    st.json(eda)

    summary_text = f"""
Dataset Shape:
{eda.get('shape')}

Columns:
{eda.get('columns')}

Data Types:
{eda.get('dtypes')}

Missing Values:
{eda.get('missing_values')}

Statistical Summary:
{eda.get('summary')}
"""

    # Generate hypotheses only when button pressed
    if st.button("🧠 Generate Hypotheses"):
        with st.spinner("Generating hypotheses..."):
            st.session_state.hypotheses = generate_hypotheses(summary_text)

    # ---- SHOW HYPOTHESES IF AVAILABLE ----
    if st.session_state.hypotheses:
        st.subheader("🧠 AI Hypotheses")

        hypothesis_list = [
            h.strip() for h in st.session_state.hypotheses.split("\n") if h.strip()
        ]

        st.session_state.selected_hypothesis = st.radio(
            "Select a hypothesis to validate:",
            hypothesis_list,
            key="hypothesis_radio"
        )

        # Validate
        if st.button("🔬 Validate Hypothesis"):
            with st.spinner("Running analysis..."):
                validation_result = validate_hypothesis(df, st.session_state.selected_hypothesis)

            st.subheader("📈 Validation Result")
            st.json(validation_result)

            st.subheader("🧠 Analyst Explanation")
            explanation = explain_result(
                st.session_state.selected_hypothesis,
                validation_result
            )
            st.write(explanation)
