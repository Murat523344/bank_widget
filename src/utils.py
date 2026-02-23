# src/utils.py
import json
from typing import Any, List, Dict


def read_json(path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл с банковскими операциями.

    :param path: путь к JSON-файлу
    :return: список операций (каждая операция — словарь) или пустой список,
             если файл пустой, не найден или содержит не список
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Пример других утилит (если будут использоваться в тестах)
def some_util_function(x: int) -> int:
    """
    Пример вспомогательной функции.
    """
    return x * 2


def another_util_function(s: str) -> str:
    """
    Пример другой вспомогательной функции.
    """
    return s.strip().upper()
