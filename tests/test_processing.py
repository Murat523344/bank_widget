import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2026-01-25"},
        {"id": 2, "state": "PENDING", "date": "2026-01-26"},
        {"id": 3, "state": "EXECUTED", "date": "2026-01-27"},
    ]


def test_filter_by_state(operations):
    filtered = filter_by_state(operations, "EXECUTED")
    assert len(filtered) == 2
    assert all(op["state"] == "EXECUTED" for op in filtered)


def test_sort_by_date(operations):
    sorted_ops = sort_by_date(operations)
    dates = [op["date"] for op in sorted_ops]
    assert dates == sorted(dates, reverse=True)
