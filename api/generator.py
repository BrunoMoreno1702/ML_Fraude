import random
from datetime import datetime, timedelta

MERCHANTS = {
    "Amazon": {"category": "shopping", "min_amount": 20, "max_amount": 300},
    "Uber": {"category": "transport", "min_amount": 8, "max_amount": 90},
    "Shell": {"category": "fuel", "min_amount": 50, "max_amount": 500},
    "Walmart": {"category": "shopping", "min_amount": 20, "max_amount": 400},
    "Starbucks": {"category": "food", "min_amount": 10, "max_amount": 60},
    "McDonalds": {"category": "food", "min_amount": 15, "max_amount": 80},
    "Subway": {"category": "food", "min_amount": 12, "max_amount": 70},
    "Carrefour": {"category": "shopping", "min_amount": 25, "max_amount": 350}
}


def generate_normal_transaction(customer_id):
    merchant = random.choice(list(MERCHANTS.keys()))
    merchant_info = MERCHANTS[merchant]

    random_hour = random.randint(8, 22)
    random_day_offset = random.randint(0, 30)

    timestamp = datetime.now().replace(
        hour=random_hour,
        minute=random.randint(0, 59),
        second=random.randint(0, 59),
        microsecond=0
    ) - timedelta(days=random_day_offset)

    return {
        "transaction_id": f"tx_{random.randint(100000, 999999)}",
        "customer_id": customer_id,
        "amount": round(random.uniform(
            merchant_info["min_amount"],
            merchant_info["max_amount"]
        ), 2),
        "merchant": merchant,
        "category": merchant_info["category"],
        "timestamp": timestamp.isoformat(),
        "is_fraud": 0
    }


def generate_fraud_transaction(customer_id):
    merchant = random.choice(list(MERCHANTS.keys()))
    merchant_info = MERCHANTS[merchant]

    random_hour = random.randint(2, 5)
    random_day_offset = random.randint(0, 90)

    timestamp = datetime.now().replace(
        hour=random_hour,
        minute=random.randint(0, 59),
        second=random.randint(0, 59),
        microsecond=0
    ) - timedelta(days=random_day_offset)

    return {
        "transaction_id": f"tx_{random.randint(100000, 999999)}",
        "customer_id": customer_id,
        "amount": round(random.uniform(1000, 5000), 2),
        "merchant": merchant,
        "category": merchant_info["category"],
        "timestamp": timestamp.isoformat(),
        "is_fraud": 1
    }


def generate_customer_transactions(customer_id):
    transactions = []

    normal_count = random.randint(7, 22)

    for _ in range(normal_count):
        transactions.append(generate_normal_transaction(customer_id))

    # 20% dos clientes terão fraudes
    if random.random() < 0.2:
        fraud_count = random.randint(3, 7)
        for _ in range(fraud_count):
            transactions.append(generate_fraud_transaction(customer_id))

    return transactions