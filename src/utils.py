import json
import logging
from typing import Any, Dict, List

# --- Логгер для модуля utils ---
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
            logger.debug(f"Файл {path} успешно прочитан, найдено {len(data)} записей")
            return data

        logger.warning(f"Файл {path} прочитан, но содержимое не является списком")
        return []

    except FileNotFoundError:
        logger.error(f"Файл {path} не найден")
        return []
    except json.JSONDecodeError:
        logger.error(f"Файл {path} содержит некорректный JSON")
        return []


def some_util_function(x: int) -> int:
    """
    Пример вспомогательной функции.
    """
    result = x * 2
    logger.debug(f"some_util_function({x}) -> {result}")
    return result


def another_util_function(s: str) -> str:
    """
    Пример другой вспомогательной функции.
    """
    result = s.strip().upper()
    logger.debug(f"another_util_function({s!r}) -> {result!r}")
    return result
