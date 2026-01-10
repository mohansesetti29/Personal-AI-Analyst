import pandas as pd
import numpy as np

def is_binary(series: pd.Series):
    return series.dropna().nunique() == 2

def validate_hypothesis(df: pd.DataFrame, hypothesis: str):
    result = {}

    # Identify numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    # Identify binary columns (Yes/No or 0/1)
    binary_cols = [
        col for col in df.columns
        if is_binary(df[col])
    ]

    # ---- CASE 1: Numeric vs Numeric → Correlation ----
    for col1 in numeric_cols:
        for col2 in numeric_cols:
            if col1 != col2 and col1 in hypothesis and col2 in hypothesis:
                corr = df[col1].corr(df[col2])
                result["test"] = "Correlation Analysis"
                result["columns"] = [col1, col2]
                result["correlation"] = corr
                result["interpretation"] = (
                    "Strong positive relationship"
                    if corr > 0.5 else
                    "Weak or no relationship"
                )
                return result

    # ---- CASE 2: Binary vs Numeric → Mean Comparison ----
    for bin_col in binary_cols:
        for num_col in numeric_cols:
            if bin_col in hypothesis and num_col in hypothesis:
                groups = df.groupby(bin_col)[num_col].mean()
                result["test"] = "Binary vs Numeric Comparison"
                result["binary_column"] = bin_col
                result["numeric_column"] = num_col
                result["group_means"] = groups.to_dict()
                result["interpretation"] = "Difference detected between groups"
                return result

    # ---- CASE 3: Binary vs Binary → Rate Comparison ----
    for col1 in binary_cols:
        for col2 in binary_cols:
            if col1 != col2 and col1 in hypothesis and col2 in hypothesis:
                rate_1 = df[df[col1] == df[col1].unique()[0]][col2].mean()
                rate_2 = df[df[col1] == df[col1].unique()[1]][col2].mean()
                result["test"] = "Binary vs Binary Comparison"
                result["columns"] = [col1, col2]
                result["rates"] = {
                    str(df[col1].unique()[0]): rate_1,
                    str(df[col1].unique()[1]): rate_2,
                }
                result["interpretation"] = "Outcome rates differ across groups"
                return result

    # ---- FALLBACK ----
    result["error"] = "Hypothesis pattern not supported yet"
    return result
