import pandas as pd

def correlation(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include="number")
    return numeric_df.corr().to_dict()
