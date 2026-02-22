import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: dict[str, Any]) -> float:
    """
    Convert transaction amount to RUB.

    :param transaction: transaction dict
    :return: amount in RUB
    """
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency")

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        headers = {"apikey": API_KEY}
        params = {"base": currency, "symbols": "RUB"}

        response = requests.get(URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        rate = response.json()["rates"]["RUB"]
        return amount * rate

    return amount