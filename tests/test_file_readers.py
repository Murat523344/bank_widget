from unittest.mock import patch

import pandas as pd

from src.file_readers import read_transactions_from_csv, read_transactions_from_excel

# Пример данных для теста
sample_data = [
    {"date": "2026-03-01", "amount": 100, "currency": "USD"},
    {"date": "2026-03-02", "amount": 200, "currency": "EUR"},
]


@patch("pandas.read_csv")
def test_read_transactions_from_csv(mock_read_csv):
    mock_df = pd.DataFrame(sample_data)
    mock_read_csv.return_value = mock_df

    result = read_transactions_from_csv("dummy_path.csv")
    assert result == sample_data
    mock_read_csv.assert_called_once_with("dummy_path.csv")


@patch("pandas.read_excel")
def test_read_transactions_from_excel(mock_read_excel):
    mock_df = pd.DataFrame(sample_data)
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel("dummy_path.xlsx")
    assert result == sample_data
    mock_read_excel.assert_called_once_with("dummy_path.xlsx")
