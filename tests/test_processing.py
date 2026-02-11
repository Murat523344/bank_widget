import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations():
    """Фикстура с примерными операциями для тестов."""
    return [
        {"amount": 100, "date": "2022-09-15", "state": "EXECUTED"},
        {"amount": 200, "date": "2022-09-16", "state": "PENDING"},
        {"amount": 150, "date": "2022-09-14", "state": "EXECUTED"},
    ]


def test_sort_by_date(sample_operations):
    """Проверка сортировки по дате (по убыванию)."""
    result = sort_by_date(sample_operations)
    assert result[0]["date"] == "2022-09-16"
    assert result[-1]["date"] == "2022-09-14"


def test_filter_by_state(sample_operations):
    """Проверка фильтрации по состоянию 'EXECUTED'."""
    result = filter_by_state(sample_operations)
    assert all(op["state"] == "EXECUTED" for op in result)
