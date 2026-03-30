import pandas as pd
import sqlite3

def extract():
    print("Extracting data...")
    return pd.read_csv("data/sales.csv")

def transform(df):
    print("Cleaning data...")

    # remove missing values
    df = df.dropna()

    # remove invalid row
    df = df[df["quantity"] > 0]

    # convert types
    df["price"] = df["price"].astype(float)
    df["quantity"] = df["quantity"].astype(int)

    # add revenue column
    df["revenue"] = df["price"] * df["quantity"]

    return df

def load(df):
    print("Saving to database...")
    conn = sqlite3.connect("sales.db")
    df.to_sql("sales_cleaned", conn, if_exists="replace", index=False)
    conn.close()

def analyze():
    print("Running analysis...")
    conn = sqlite3.connect("sales.db")

    query = """
    SELECT country, SUM(revenue) as total_revenue
    FROM sales_cleaned
    GROUP BY country
    ORDER BY total_revenue DESC
    """

    result = pd.read_sql(query, conn)
    print(result)

    conn.close()

def main():
    df = extract()
    df = transform(df)
    load(df)
    analyze()

if __name__ == "__main__":
    main()