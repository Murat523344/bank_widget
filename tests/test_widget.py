import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account, card, expected_account, expected_card",
    [
        (
            "12345678901234567890",
            "1234567890123456",
            "****567890",
            "1234 56** **** 3456",
        ),
        ("1234", "1234", "1234", "1234"),
    ],
)
def test_mask_account_card(
    account: str,
    card: str,
    expected_account: str,
    expected_card: str,
) -> None:
    masked_account, masked_card = mask_account_card(account, card)
    assert masked_account == expected_account
    assert masked_card == expected_card


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2026-01-28", "28.01.2026"),
        ("invalid", "invalid"),
        (None, None),
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected
