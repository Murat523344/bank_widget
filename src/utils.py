import json
from typing import Any


def read_json(path: str) -> list[dict[str, Any]]:
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
