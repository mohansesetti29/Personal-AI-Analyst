import pandas as pd

def validate_hypothesis(df: pd.DataFrame, hypothesis: str):
    result = {}

    if "monthly_spend" in hypothesis and "orders_count" in hypothesis:
        corr = df["monthly_spend"].corr(df["orders_count"])
        result["test"] = "Correlation Test"
        result["correlation"] = corr
        result["interpretation"] = (
            "Strong positive relationship"
            if corr > 0.5 else
            "Weak or no relationship"
        )

    elif "Male" in hypothesis and "Female" in hypothesis:
        male_avg = df[df["gender"] == "Male"]["monthly_spend"].mean()
        female_avg = df[df["gender"] == "Female"]["monthly_spend"].mean()
        result["test"] = "Mean Comparison"
        result["male_avg_spend"] = male_avg
        result["female_avg_spend"] = female_avg
        result["interpretation"] = (
            "Male customers spend more on average"
            if male_avg > female_avg else
            "Female customers spend more on average"
        )

    elif "churned" in hypothesis and "orders_count" in hypothesis:
        churned_avg = df[df["churned"] == "Yes"]["orders_count"].mean()
        active_avg = df[df["churned"] == "No"]["orders_count"].mean()
        result["test"] = "Churn Comparison"
        result["churned_avg_orders"] = churned_avg
        result["active_avg_orders"] = active_avg
        result["interpretation"] = (
            "Lower order count is associated with churn"
            if churned_avg < active_avg else
            "No strong churn signal detected"
        )

    else:
        result["error"] = "Hypothesis not supported yet"

    return result
