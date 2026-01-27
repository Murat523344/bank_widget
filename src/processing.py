def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует операции по статусу state.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: list, reverse: bool = True) -> list:
    """
    Сортирует операции по дате.
    """
    return sorted(
        operations,
        key=lambda op: op.get("date", ""),
        reverse=reverse
    )
