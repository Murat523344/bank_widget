# src/main.py
from typing import List, Dict
from src.processing import (
    filter_by_state,
    sort_by_date,
    process_bank_search,
    process_bank_operations,
)
from src.file_readers import (
    read_transactions_from_json,
    read_transactions_from_csv,
    read_transactions_from_excel,
)


def main() -> None:
    """
    Основная функция программы.
    Предоставляет пользователю интерфейс для работы с банковскими транзакциями:
    - выбор источника данных (JSON, CSV, XLSX),
    - фильтрация по статусу операций,
    - сортировка по дате,
    - фильтрация по валюте (рубли),
    - фильтрация по ключевому слову в описании,
    - вывод результатов.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

    # Выбор источника данных
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input("Ваш выбор (1/2/3): ").strip()
        if choice in {"1", "2", "3"}:
            break
        print("Некорректный выбор. Попробуйте снова.")

    if choice == "1":
        file_path = input("Введите путь к JSON-файлу: ").strip()
        data: List[Dict[str, str]] = read_transactions_from_json(file_path)
    elif choice == "2":
        file_path = input("Введите путь к CSV-файлу: ").strip()
        data = read_transactions_from_csv(file_path)
    else:
        file_path = input("Введите путь к XLSX-файлу: ").strip()
        data = read_transactions_from_excel(file_path)

    # Фильтрация по статусу
    valid_states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        state = input(f"Введите статус для фильтрации ({', '.join(valid_states)}): ").strip().upper()
        if state in valid_states:
            break
        print(f'Статус "{state}" недоступен. Попробуйте снова.')
    data = filter_by_state(data, state)
    print(f"\nОперации отфильтрованы по статусу '{state}'\n")

    # Сортировка по дате
    sort_input = input("Отсортировать операции по дате? (Да/Нет): ").strip().lower()
    if sort_input == "да":
        order = input("По возрастанию или по убыванию? ").strip().lower()
        descending = order != "по возрастанию"
        data = sort_by_date(data, descending)

    # Фильтрация по валюте (рубли)
    filter_rub = input("Выводить только рублевые транзакции? (Да/Нет): ").strip().lower()
    if filter_rub == "да":
        data = [op for op in data if op.get("currency") == "RUB"]

    # Фильтрация по ключевому слову
    filter_search = input("Отфильтровать по слову в описании? (Да/Нет): ").strip().lower()
    if filter_search == "да":
        search_str = input("Введите слово для поиска: ").strip()
        data = process_bank_search(data, search_str)

    # Вывод результата
    if not data:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"\nВсего операций в выборке: {len(data)}\n")
        for op in data:
            print(f"{op.get('date')} | {op.get('description')} | {op.get('amount')} {op.get('currency')}")


if __name__ == "__main__":
    main()
