# src/file_readers.py
from typing import Any, Dict, List, cast

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла с разделителем ';'.

    :param file_path: путь к CSV-файлу
    :return: список словарей с транзакциями
    """
    df = pd.read_csv(file_path, sep=";")
    return cast(List[Dict[str, Any]], df.to_dict(orient="records"))


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла (.xlsx).

    :param file_path: путь к Excel-файлу
    :return: список словарей с транзакциями
    """
    df = pd.read_excel(file_path)
    return cast(List[Dict[str, Any]], df.to_dict(orient="records"))
