<<<<<<< HEAD
Bank Widget
Описание проекта
Проект представляет собой модуль для подготовки данных о банковских операциях клиента. Он используется для виджета в личном кабинете клиента, который отображает последние операции с картами и счетами.
Проект разделён на несколько модулей:
masks — функции для маскировки номеров банковских карт и счетов.
widget — функции для работы с отображением информации о картах и счетах (mask_account_card, get_date).
processing — функции для фильтрации и сортировки операций (filter_by_state, sort_by_date).
Установка
Клонировать репозиторий:
git clone <URL_репозитория>
cd bank_widget
Создать и активировать виртуальное окружение через Poetry:
poetry install
poetry shell
Использование функций
Маскировка карт и счетов
from src.widget.widget import mask_account_card, get_date

mask_account_card("Visa Platinum 7000792289606361")
# Вывод: 'Visa Platinum 7000 79** **** 6361'

mask_account_card("Счет 73654108430135874305")
# Вывод: 'Счет **4305'

get_date("2024-03-11T02:26:18.671407")
# Вывод: '11.03.2024'
Фильтрация операций по статусу
from src.processing.processing import filter_by_state

data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01T12:00:00'},
    {'id': 2, 'state': 'CANCELED', 'date': '2024-01-02T12:00:00'},
]

filter_by_state(data)
# Вывод: [{'id': 1, 'state': 'EXECUTED', 'date': '2024-01-01T12:00:00'}]

filter_by_state(data, state='CANCELED')
# Вывод: [{'id': 2, 'state': 'CANCELED', 'date': '2024-01-02T12:00:00'}]
Сортировка операций по дате
from src.processing.processing import sort_by_date

sort_by_date(data)
# Вывод: операции в порядке убывания даты (сначала новые)
Проверка кода
Flake8: poetry run flake8 src/
isort: poetry run isort src/
mypy: poetry run mypy --package src
Структура проекта
bank_widget/
├── src/
│   ├── masks.py
│   ├── widget/
│   │   └── widget.py
│   └── processing/
│       └── processing.py
├── tests/
├── main.py
├── pyproject.toml
├── poetry.lock
└── README.md
=======
# Тестирование проекта

Запуск всех тестов:
```bash
pytest

Запуск тестов с покрытием кода:
pytest --cov=src --cov-report=html

Отчет с покрытием появится в папке htmlcov.

---

# **Шаг 3. Создание фикстур**

Фикстуры создают тестовые данные один раз и позволяют использовать их в нескольких тестах.

1. Создай файл `tests/conftest.py` (если его ещё нет):
```python
# tests/conftest.py
import pytest

# Фикстура для операций
@pytest.fixture
def sample_operations():
    return [
        {"state": "EXECUTED", "date": "2022-09-15", "amount": 100},
        {"state": "PENDING", "date": "2022-09-16", "amount": 200},
        {"state": "EXECUTED", "date": "2022-09-14", "amount": 150},
    ]

# Фикстура для карт
@pytest.fixture
def sample_cards():
    return ["1234567890123456", "9876543210987654", "1111222233334444"]

# Фикстура для счетов
@pytest.fixture
def sample_accounts():
    return ["12345678901234567890", "09876543210987654321"]

>>>>>>> homework_10_2

## Новая функциональность

В этом обновлении добавлены функции для работы с финансовыми операциями:

1. **Чтение из CSV**  
   Функция `read_csv_transactions(path)` принимает путь к CSV-файлу и возвращает список словарей с транзакциями.

2. **Чтение из Excel**  
   Функция `read_excel_transactions(path)` принимает путь к Excel-файлу и возвращает список словарей с транзакциями.

### Пример использования

```python
from src.utils import read_csv_transactions, read_excel_transactions

csv_data = read_csv_transactions("transactions.csv")
excel_data = read_excel_transactions("transactions.xlsx")

print(csv_data)
print(excel_data)