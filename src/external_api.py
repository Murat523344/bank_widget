import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()  # загружаем переменные из .env

EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует транзакцию в рубли.
    """
    amount = transaction.get("amount", 0)
    currency = transaction.get("currency", "RUB").upper()

    if currency == "RUB":
        return float(amount)

    if currency in ("USD", "EUR"):
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
        headers = {"apikey": EXCHANGE_API_KEY}
        response = requests.get(url, headers=headers)
        data = response.json()
        rate = data["rates"]["RUB"]
        return float(amount) * float(rate)

    return float(amount)


def api_call() -> Dict[str, Any]:
    """
    Заглушка для теста API вызова.
    """
    return {"status": "success", "data": {"id": 1, "name": "test"}}


def process_api_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Заглушка обработки данных API.
    """
    return {"processed": True, **data}
