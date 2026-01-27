import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations():
    return [
        {"state": "EXECUTED", "date": "2022-09-15", "amount": 100},
        {"state": "PENDING", "date": "2022-09-16", "amount": 200},
        {"state": "EXECUTED", "date": "2022-09-14", "amount": 150},
    ]


def test_filter_by_state(sample_operations):
    result = filter_by_state(sample_operations, "EXECUTED")
    assert all(op["state"] == "EXECUTED" for op in result)


def test_sort_by_date(sample_operations):
    result = sort_by_date(sample_operations, reverse=True)
    dates = [op["date"] for op in result]
    assert dates == sorted(dates, reverse=True)
