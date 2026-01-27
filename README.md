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

