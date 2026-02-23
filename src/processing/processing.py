from typing import Dict, List


def sort_by_date(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по ключу 'date' в порядке возрастания.
    """
    return sorted(data, key=lambda x: x.get("date", ""))


def filter_by_state(data: List[Dict[str, str]], state: str) -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по полю 'state'.
    """
    return [item for item in data if item.get("state") == state]
