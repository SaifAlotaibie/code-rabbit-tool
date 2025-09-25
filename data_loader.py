# data_loader.py
import pandas as pd

def load_data():
    # ⚠️ file path hardcoded
    df = pd.read_csv("data.csv")

    # ⚠️ missing handling for missing values
    return df

def preprocess_data(df):
    # ⚠️ no scaling or encoding, just dropping nulls
    df = df.dropna()
    return df
