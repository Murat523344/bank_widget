import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("value,expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("12345678901234567890", "****567890"),
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize("input_date,expected", [
    ("2022-09-15", "15.09.2022"),
    ("2022/09/15", "15.09.2022"),
])
def test_get_date(input_date, expected):
    assert get_date(input_date) == expected
