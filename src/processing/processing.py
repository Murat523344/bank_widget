import re
from collections import Counter
from datetime import datetime
from typing import Dict, List


def filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей с информацией о банковских операциях.
    :param state: Значение ключа 'state', по которому фильтруем. По умолчанию 'EXECUTED'.
    :return: Новый список словарей, где ключ 'state' равен указанному значению.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, str]], descending: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по дате.

    :param data: Список словарей с ключом 'date' в формате ISO.
    :param descending: Порядок сортировки. True — от новых к старым, False — от старых к новым.
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(
        data,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=descending
    )


def process_bank_search(data: List[Dict[str, str]], search: str) -> List[Dict[str, str]]:
    """
    Ищет транзакции, где в поле 'description' встречается строка поиска.

    :param data: Список транзакций.
    :param search: Строка поиска.
    :return: Список словарей с подходящими транзакциями.
    """
    pattern = re.compile(search, re.IGNORECASE)
    return [item for item in data if pattern.search(item.get("description", ""))]


def process_bank_operations(data: List[Dict[str, str]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям.

    :param data: Список транзакций.
    :param categories: Список категорий для подсчёта.
    :return: Словарь {категория: количество операций}.
    """
    # Берём только существующие описания, которые есть в списке категорий
    descriptions: List[str] = [
        item["description"]
        for item in data
        if isinstance(item.get("description"), str) and item["description"] in categories
    ]
    return dict(Counter(descriptions))
