import pandas as pd
import sqlite3

def extract():
    print("Extracting data...")
    return pd.read_csv("data/sales.csv")