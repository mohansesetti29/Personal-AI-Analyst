from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import pandas as pd

from backend.tools.eda import run_eda
from backend.agent import generate_hypotheses, explain_result
from backend.tools.validate import validate_hypothesis

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AnalystGPT",
    layout="wide"
)

st.title("📊 AnalystGPT – Personal AI Data Analyst")

# ---------------- SESSION STATE ----------------
if "hypotheses" not in st.session_state:
    st.session_state.hypotheses = None

if "selected_hypothesis" not in st.session_state:
    st.session_state.selected_hypothesis = None

if "validation_result" not in st.session_state:
    st.session_state.validation_result = None

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # -------- DATA PREVIEW --------
    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # -------- EDA --------
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

    # -------- HYPOTHESIS GENERATION --------
    if st.button("🧠 Generate Hypotheses"):
        with st.spinner("Generating hypotheses..."):
            st.session_state.hypotheses = generate_hypotheses(summary_text)
            st.session_state.validation_result = None

    # -------- SHOW HYPOTHESES --------
    if st.session_state.hypotheses:
        st.subheader("🧠 AI Hypotheses")

        hypothesis_list = [
            h.strip()
            for h in st.session_state.hypotheses.split("\n")
            if h.strip()
        ]

        st.session_state.selected_hypothesis = st.radio(
            "Select a hypothesis to validate:",
            hypothesis_list
        )

        # -------- VALIDATION --------
        if st.button("🔬 Validate Hypothesis"):
            with st.spinner("Running statistical validation..."):
                st.session_state.validation_result = validate_hypothesis(
                    df,
                    st.session_state.selected_hypothesis
                )

        # -------- SHOW RESULTS --------
        if st.session_state.validation_result is not None:
            st.subheader("📈 Validation Result")
            st.json(st.session_state.validation_result)

            # -------- SAFE EXPLANATION --------
            if "error" in st.session_state.validation_result:
                st.warning(
                    "⚠️ This hypothesis could not be validated yet.\n\n"
                    "Reason: The current validation engine does not support "
                    "this hypothesis pattern. You can extend the validator "
                    "to handle this case."
                )
            else:
                st.subheader("🧠 Analyst Explanation")
                explanation = explain_result(
                    st.session_state.selected_hypothesis,
                    st.session_state.validation_result
                )
                st.write(explanation)
