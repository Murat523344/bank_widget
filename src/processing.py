from typing import List, Dict


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует операции по статусу state.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует операции по дате в порядке убывания.
    """
    return sorted(
        operations,
        key=lambda op: op.get("date", ""),
        reverse=reverse
    )
