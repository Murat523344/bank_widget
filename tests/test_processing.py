from typing import Dict, List

import pytest

from src.processing.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "data, state, expected",
    [
        ([], "EXECUTED", []),
        ([{"state": "EXECUTED"}], "EXECUTED", [{"state": "EXECUTED"}]),
    ]
)
def test_filter_by_state(data: List[Dict], state: str, expected: List[Dict]) -> None:
    result = filter_by_state(data, state)
    assert result == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        ([], []),
        ([{"date": "2020-01-01"}, {"date": "2019-01-01"}],
         [{"date": "2019-01-01"}, {"date": "2020-01-01"}]),
    ]
)
def test_sort_by_date(data: List[Dict], expected: List[Dict]) -> None:
    result = sort_by_date(data)
    assert result == expected
