import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


# ------------------------
# Тесты filter_by_currency
# ------------------------
@pytest.mark.parametrize(
    "transactions, currency_code, expected_ids",
    [
        (
            [
                {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
                {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}},
            ],
            "USD",
            [1],
        ),
        (
            [{"id": 3, "operationAmount": {"currency": {"code": "RUB"}}}],
            "USD",
            [],
        ),
        ([], "USD", []),
    ],
)
def test_filter_by_currency_param(transactions, currency_code, expected_ids):
    result = list(filter_by_currency(transactions, currency_code))
    assert [t["id"] for t in result] == expected_ids


# -------------------------------
# Тесты transaction_descriptions
# -------------------------------
@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [{"description": "Перевод A"}, {"description": "Перевод B"}],
            ["Перевод A", "Перевод B"],
        ),
        ([], []),
        ([{}], []),
    ],
)
def test_transaction_descriptions_param(transactions, expected):
    result = list(transaction_descriptions(transactions))
    assert result == expected


# ------------------------
# Тесты card_number_generator
# ------------------------
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
        (5, 5, ["0000 0000 0000 0005"]),
        (
            0,
            2,
            [
                "0000 0000 0000 0000",
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
            ],
        ),
    ],
)
def test_card_number_generator_param(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
