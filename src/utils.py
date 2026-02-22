import json
from typing import Any


def read_operations(path: str) -> list[dict[str, Any]]:
    """
    Read JSON file with operations.

    :param path: path to JSON file
    :return: list of operations or empty list
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []