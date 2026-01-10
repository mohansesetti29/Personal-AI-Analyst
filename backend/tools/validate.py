import pandas as pd
import numpy as np

def validate_hypothesis(df: pd.DataFrame, columns: list, h_type: str):
    result = {}

    if h_type == "numeric_vs_numeric":
        col1, col2 = columns
        corr = df[col1].corr(df[col2])
        result.update({
            "test": "Correlation Analysis",
            "columns": columns,
            "correlation": corr,
            "interpretation": (
                "Strong positive relationship" if corr > 0.5 else
                "Weak or no relationship"
            )
        })
        return result

    if h_type == "binary_vs_numeric":
        bin_col, num_col = columns
        means = df.groupby(bin_col)[num_col].mean().to_dict()
        result.update({
            "test": "Binary vs Numeric Comparison",
            "binary_column": bin_col,
            "numeric_column": num_col,
            "group_means": means,
            "interpretation": "Difference detected between groups"
        })
        return result

    if h_type == "binary_vs_binary":
        col1, col2 = columns
        rates = df.groupby(col1)[col2].mean().to_dict()
        result.update({
            "test": "Binary vs Binary Comparison",
            "columns": columns,
            "rates": rates,
            "interpretation": "Outcome rates differ across groups"
        })
        return result

    return {"error": "Unsupported hypothesis type"}
