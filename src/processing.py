<<<<<<< HEAD
def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список операций по состоянию (state).
=======
def filter_by_state(operations: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует операции по статусу state.
>>>>>>> fe4f832 (Домашка: проект с src и тестами)
    """
    return [op for op in operations if op.get("state") == state]


<<<<<<< HEAD
def sort_by_date(operations: list[dict]) -> list[dict]:
    """
    Сортировка операций по дате в порядке убывания.
    """
    return sorted(operations, key=lambda x: x["date"], reverse=True)
=======
def sort_by_date(operations: list, reverse: bool = True) -> list:
    """
    Сортирует операции по дате.
    """
    return sorted(
        operations,
        key=lambda op: op.get("date", ""),
        reverse=reverse
    )
>>>>>>> fe4f832 (Домашка: проект с src и тестами)
