import os

import requests
from dotenv import load_dotenv

load_dotenv()  # загружаем переменные из .env

EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует транзакцию в рубли.
    Если валюта USD или EUR, обращается к API для конвертации.
    Если RUB — возвращает сумму без изменений.

    :param transaction: словарь с ключами "amount" и "currency"
    :return: сумма в рублях (float)
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

    # если неизвестная валюта — возвращаем сумму без изменений
    return float(amount)
