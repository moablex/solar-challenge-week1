import pandas as pd

def load_data(country):
    return pd.read_csv(f"../data/{country}_clean.csv", index_col="Timestamp", parse_dates=True)

def get_ghi_summary(df):
    return {"mean": df["GHI"].mean(), "median": df["GHI"].median(), "std": df["GHI"].std()}