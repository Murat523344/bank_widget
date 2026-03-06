from typing import Any, Dict, List

from src.processing import (
    filter_by_state,
    process_bank_operations,
    process_bank_search,
    sort_by_date,
)


def main() -> None:
    """Основная функция запуска программы."""

    print("Добро пожаловать в программу работы с банковскими операциями!")

    operations: List[Dict[str, Any]] = [
        {
            "state": "EXECUTED",
            "description": "Открытие вклада",
            "date": "2019-12-08",
            "amount": 40542,
            "currency": "RUB",
        },
        {
            "state": "EXECUTED",
            "description": "Перевод с карты на карту",
            "date": "2019-11-12",
            "amount": 130,
            "currency": "USD",
        },
        {
            "state": "CANCELED",
            "description": "Перевод организации",
            "date": "2018-07-18",
            "amount": 8390,
            "currency": "RUB",
        },
        {
            "state": "EXECUTED",
            "description": "Перевод со счета на счет",
            "date": "2018-06-03",
            "amount": 8200,
            "currency": "RUB",
        },
    ]

    # выбор статуса
    status = input(
        "Введите статус операций для фильтрации (EXECUTED, CANCELED, PENDING): "
    ).upper()

    operations = filter_by_state(operations, status)

    # сортировка
    sort_answer = input("Отсортировать операции по дате? (да/нет): ").lower()

    if sort_answer == "да":
        order = input("Сортировать по возрастанию или убыванию? (asc/desc): ").lower()

        descending = order != "asc"
        operations = sort_by_date(operations, descending)

    # поиск
    search = input("Введите строку для поиска в описании операций: ")

    if search:
        operations = process_bank_search(operations, search)

    # категории
    categories = ["Открытие вклада", "Перевод с карты на карту", "Перевод организации"]
    stats = process_bank_operations(operations, categories)

    print("\nСтатистика операций:")
    for category, count in stats.items():
        print(f"{category}: {count}")

    print("\nСписок операций:")
    for op in operations:
        print(
            f"{op['date']} | {op['description']} | "
            f"{op['amount']} {op['currency']} | {op['state']}"
        )


if __name__ == "__main__":
    main()
