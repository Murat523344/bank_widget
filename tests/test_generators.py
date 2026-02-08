import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "operationAmount": {"amount": "100", "currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "operationAmount": {"amount": "200", "currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "operationAmount": {"amount": "300", "currency": {"code": "USD"}},
            "description": "Перевод с карты на карту",
        },
    ]


def test_filter_by_currency_usd(transactions):
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_filter_by_currency_not_found(transactions):
    result = list(filter_by_currency(transactions, "EUR"))
    assert result == []


def test_filter_by_currency_empty():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(transactions):
    result = list(transaction_descriptions(transactions))
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert result == []


def test_card_number_generator_range():
    result = list(card_number_generator(1, 3))
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]


def test_card_number_generator_single():
    result = list(card_number_generator(5, 5))
    assert result == ["0000 0000 0000 0005"]


def test_card_number_generator_format():
    number = next(card_number_generator(1, 1))
    assert len(number) == 19  # 16 цифр + 3 пробела
    assert number.count(" ") == 3
