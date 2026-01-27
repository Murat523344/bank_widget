def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список операций по состоянию (state).
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: list[dict]) -> list[dict]:
    """
    Сортировка операций по дате в порядке убывания.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=True)
