from fastapi import FastAPI
from api.generator import generate_customer_transactions

app = FastAPI()


@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/transactions")
def get_transactions(customers: int = 100):

    data = []

    for i in range(1, customers + 1):

        customer_id = f"CUST_{i:05d}"

        data.extend(
            generate_customer_transactions(customer_id)
        )

    return {
        "customers": customers,
        "transactions": len(data),
        "data": data
    }