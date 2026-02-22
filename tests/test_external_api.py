import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub

@patch("src.external_api.requests.get")
def test_convert_usd(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 80}}
    transaction = {"amount": 10, "currency": "USD"}
    result = convert_to_rub(transaction)
    assert isinstance(result, float)
    assert result == 10 * 80

@patch("src.external_api.requests.get")
def test_convert_eur(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 90}}
    transaction = {"amount": 5, "currency": "EUR"}
    result = convert_to_rub(transaction)
    assert result == 5 * 90

def test_convert_rub():
    transaction = {"amount": 500, "currency": "RUB"}
    result = convert_to_rub(transaction)
    assert result == 500