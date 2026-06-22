import pandas as pd

df = pd.read_csv("../data/transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# features temporais
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.day
df["month"] = df["timestamp"].dt.month

# encoding categórico
df["merchant_code"] = df["merchant"].astype("category").cat.codes
df["category_code"] = df["category"].astype("category").cat.codes
df["customer_code"] = df["customer_id"].astype("category").cat.codes

# FEATURES BASE
features = [
    "amount",
    "hour",
    "day",
    "month",
    "merchant_code",
    "category_code",
    "customer_code"
]

X = df[features]
y = df["is_fraud"]

X.to_csv("../data/X.csv", index=False)
y.to_csv("../data/y.csv", index=False)

print("Dataset pronto")
print("Shape:", X.shape)