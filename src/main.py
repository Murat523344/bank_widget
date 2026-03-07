from typing import Any, Dict, List

from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


def main() -> None:
    """Основная функция запуска программы."""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ").strip()
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Работа программы завершена.")
        return

    # Пример операций (можно потом брать из файла)
    operations: List[Dict[str, Any]] = [
        {"state": "EXECUTED", "description": "Открытие вклада", "date": "2019-12-08", "amount": 40542, "currency": "RUB"},
        {"state": "EXECUTED", "description": "Перевод с карты на карту", "date": "2019-11-12", "amount": 130, "currency": "USD"},
        {"state": "CANCELED", "description": "Перевод организации", "date": "2018-07-18", "amount": 8390, "currency": "RUB"},
        {"state": "EXECUTED", "description": "Перевод со счета на счет", "date": "2018-06-03", "amount": 8200, "currency": "EUR"},
    ]

    # выбор статуса
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).strip().upper()
        if status in valid_statuses:
            break
        print(f'Статус операции "{status}" недоступен.')

    operations = filter_by_state(operations, status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    # сортировка
    sort_answer = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_answer == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        descending = order not in ["возрастанию", "asc"]
        operations = sort_by_date(operations, descending)

    # фильтр по рублевой валюте
    rub_only = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if rub_only == "да":
        operations = [op for op in operations if op["currency"].upper() == "RUB"]

    # поиск по слову
    search_answer = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if search_answer == "да":
        search_word = input("Введите слово для поиска: ").strip()
        operations = process_bank_search(operations, search_word)

    # категории для статистики
    categories = ["Открытие вклада", "Перевод с карты на карту", "Перевод организации"]
    stats = process_bank_operations(operations, categories)

    print("\nСтатистика операций:")
    for category, count in stats.items():
        print(f"{category}: {count}")

    print("\nРаспечатываю итоговый список транзакций...")
    if not operations:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(operations)}\n")
        for op in operations:
            print(f"{op['date']} {op['description']}")
            print(f"Сумма: {op['amount']} {op['currency']}\n")


if __name__ == "__main__":
    main()
