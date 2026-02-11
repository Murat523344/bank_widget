"""Модуль с генераторами для обработки транзакций."""

from typing import Iterator, List, Dict


def filter_by_currency(
        transactions: List[Dict],
        currency_code: str
) -> Iterator[Dict]:
    """
    Фильтрует транзакции по коду валюты.

    Args:
        transactions (List[Dict]): Список транзакций.
        currency_code (str): Код валюты для фильтрации (например, "USD").

    Yields:
        Iterator[Dict]: Транзакции с заданной валютой.
    """
    for transaction in transactions:
        try:
            if (
                    transaction["operationAmount"]["currency"]["code"]
                    == currency_code
            ):
                yield transaction
        except KeyError:
            continue


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, возвращающий описание каждой транзакции.

    Args:
        transactions (List[Dict]): Список транзакций.

    Yields:
        Iterator[str]: Описание каждой транзакции.
    """
    for transaction in transactions:
        description = transaction.get("description")
        if description:
            yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start (int): Начальное число для генерации.
        stop (int): Конечное число для генерации.

    Yields:
        Iterator[str]: Номер карты в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, stop + 1):
        card_number = str(number).zfill(16)
        yield (
            f"{card_number[:4]} "
            f"{card_number[4:8]} "
            f"{card_number[8:12]} "
            f"{card_number[12:]}"
        )
