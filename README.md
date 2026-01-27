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
