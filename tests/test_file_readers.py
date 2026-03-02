from unittest.mock import patch

import pandas as pd

from src.file_readers import read_transactions_from_csv, read_transactions_from_excel


@patch("src.file_readers.pd.read_csv")
def test_read_transactions_from_csv(mock_read_csv):
    # имитируем CSV
    mock_df = pd.DataFrame([
        {"id": 1, "amount": 100, "category": "food"},
        {"id": 2, "amount": 200, "category": "transport"},
    ])
    mock_read_csv.return_value = mock_df

    result = read_transactions_from_csv("fake_path.csv")

    assert result == [
        {"id": 1, "amount": 100, "category": "food"},
        {"id": 2, "amount": 200, "category": "transport"},
    ]


@patch("src.file_readers.pd.read_excel")
def test_read_transactions_from_excel(mock_read_excel):
    # имитируем Excel
    mock_df = pd.DataFrame([
        {"id": 3, "amount": 300, "category": "entertainment"},
    ])
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel("fake_path.xlsx")

    assert result == [
        {"id": 3, "amount": 300, "category": "entertainment"},
    ]
