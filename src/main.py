import json

from src.file_readers import read_transactions_from_csv, read_transactions_from_excel
from src.processing import filter_by_state, process_bank_search, sort_by_date


def main() -> None:
    """Основная функция программы."""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")

    operations = []

    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        with open("data/transactions.json", encoding="utf-8") as file:
            operations = json.load(file)

    elif choice == "2":
        print("Для обработки выбран CSV-файл.")
        operations = read_transactions_from_csv("data/transactions.csv")

    elif choice == "3":
        print("Для обработки выбран Excel-файл.")
        operations = read_transactions_from_excel("data/transactions_excel.xlsx")

    else:
        print("Неверный выбор.")
        return

    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    status = input()

    operations = filter_by_state(operations, status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    sort_answer = input("Отсортировать операции по дате? Да/Нет: ").lower()

    if sort_answer == "да":
        operations = sort_by_date(operations)

    rub_answer = input("Выводить только рублевые транзакции? Да/Нет: ").lower()

    if rub_answer == "да":
        operations = [
            op for op in operations
            if op.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]

    search_answer = input(
        "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
    ).lower()

    if search_answer == "да":
        word = input("Введите слово для поиска: ")
        operations = process_bank_search(operations, word)

    print("\nРаспечатываю итоговый список транзакций...\n")

    if not operations:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    for op in operations:
        print(op)


if __name__ == "__main__":
    main()
