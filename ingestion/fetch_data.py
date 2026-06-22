import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/transactions"

def fetch_data(limit=1000):
    r = requests.get(f"{API_URL}?limit={limit}")
    data = r.json()["results"]

    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    df = fetch_data(1000)

    # garante consistência de tipo
    df["customer_id"] = df["customer_id"].astype(str)

    df.to_csv("../data/transactions.csv", index=False)

    print(df.head())
    print("\nCustomers únicos:", df["customer_id"].nunique())