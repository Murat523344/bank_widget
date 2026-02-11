from datetime import datetime
from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: Список словарей с информацией о банковских операциях.
    :param state: Значение ключа 'state', по которому фильтруем.
    По умолчанию 'EXECUTED'.
    :return: Новый список словарей, где ключ 'state' равен указанному значению.
    """
    return [
        item
        for item in data
        if item.get("state") == state
    ]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате.

    :param data: Список словарей с ключом 'date' в формате ISO.
    :param descending: Порядок сортировки.
    True — от новых к старым, False — от старых к новым.
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(
        data,
        key=lambda x: datetime.fromisoformat(
            x["date"]
        ),
        reverse=descending
    )
