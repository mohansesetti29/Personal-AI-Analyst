from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import pandas as pd
import json

from backend.tools.eda import run_eda
from backend.agent import generate_hypotheses
from backend.tools.validate import validate_hypothesis
from backend.explainer import explain_result


st.set_page_config(page_title="AnalystGPT", layout="wide")
st.title("📊 AnalystGPT – Personal AI Data Analyst")

# ---------- SESSION STATE ----------
if "hypotheses" not in st.session_state:
    st.session_state.hypotheses = None
if "selected_index" not in st.session_state:
    st.session_state.selected_index = None
if "validation" not in st.session_state:
    st.session_state.validation = None

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    eda = run_eda(df)
    st.subheader("🔍 Dataset Summary")
    st.json(eda)

    summary_text = f"""
Shape: {eda['shape']}
Columns: {eda['columns']}
Dtypes: {eda['dtypes']}
Missing: {eda['missing_values']}
Summary: {eda['summary']}
"""

    if st.button("🧠 Generate Hypotheses"):
        with st.spinner("Generating hypotheses..."):
            st.session_state.hypotheses = generate_hypotheses(summary_text)
            st.session_state.validation = None

    if st.session_state.hypotheses:
        st.subheader("🧠 AI Hypotheses")

        labels = [h["hypothesis"] for h in st.session_state.hypotheses]

        st.session_state.selected_index = st.radio(
            "Select a hypothesis to validate:",
            range(len(labels)),
            format_func=lambda i: labels[i]
        )

        if st.button("🔬 Validate Hypothesis"):
            h = st.session_state.hypotheses[st.session_state.selected_index]
            st.session_state.validation = validate_hypothesis(
                df,
                h["columns"],
                h["type"]
            )

    if st.session_state.validation:
        st.subheader("📈 Validation Result")
        st.json(st.session_state.validation)

        if "error" in st.session_state.validation:
            st.warning("This hypothesis could not be validated.")
        else:
            st.subheader("🧠 Analyst Explanation")
            explanation = explain_result(
                st.session_state.hypotheses[st.session_state.selected_index]["hypothesis"],
                st.session_state.validation
            )
            st.write(explanation)
