import pytest

from processing.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


@pytest.fixture
def sample_operations():
    return [
        {"amount": 100, "date": "2022-09-15", "state": "EXECUTED", "description": "Перевод организации"},
        {"amount": 200, "date": "2022-09-16", "state": "PENDING", "description": "Открытие вклада"},
        {"amount": 150, "date": "2022-09-14", "state": "EXECUTED", "description": "Перевод карты"},
    ]


def test_sort_by_date(sample_operations):
    result = sort_by_date(sample_operations)
    assert result[0]["date"] == "2022-09-16"
    assert result[-1]["date"] == "2022-09-14"


def test_filter_by_state(sample_operations):
    result = filter_by_state(sample_operations)
    assert all(op["state"] == "EXECUTED" for op in result)


def test_process_bank_search(sample_operations):
    # Ищем слово "перевод" (регистронезависимо)
    result = process_bank_search(sample_operations, "перевод")
    assert len(result) == 2
    for op in result:
        assert "перевод" in op["description"].lower()


def test_process_bank_operations(sample_operations):
    categories = ["Перевод организации", "Открытие вклада"]
    result = process_bank_operations(sample_operations, categories)
    assert result == {"Перевод организации": 1, "Открытие вклада": 1}
