from src.file_readers import (
    read_transactions_from_csv,
    read_transactions_from_excel,
)


def print_preview(title: str, data: list[dict], limit: int = 5) -> None:
    print(f"\n{'=' * 60}")
    print(f"{title}")
    print(f"{'=' * 60}")

    if not data:
        print("Файл пустой.")
        return

    for i, row in enumerate(data[:limit], start=1):
        print(f"{i}. {row}")


def main() -> None:
    try:
        csv_data = read_transactions_from_csv("data/transactions.csv")
        print_preview("CSV — первые 5 строк", csv_data)
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")

    try:
        excel_data = read_transactions_from_excel("data/transactions_excel.xlsx")
        print_preview("Excel — первые 5 строк", excel_data)
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")


if __name__ == "__main__":
    main()
