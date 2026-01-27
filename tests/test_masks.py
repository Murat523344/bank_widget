import pytest
from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize("card,expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("1234", "1234"),
    ("", ""),
])
def test_get_mask_card_number(card, expected):
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize("account,expected", [
    ("12345678901234567890", "****567890"),
    ("12345", "12345"),
])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
