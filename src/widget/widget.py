# Импорты всегда в начале файла
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Маскирует номер банковской карты или счета.
    """
    if info.startswith("Счет"):
        return f"Счет {get_mask_account(int(info.split()[-1]))}"
    else:
        parts = info.split()
        card_number = int(parts[-1])
        card_name = " ".join(parts[:-1])
        return f"{card_name} {get_mask_card_number(card_number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует строку даты из формата ISO в формат "ДД.ММ.ГГГГ".

    Аргументы:
        date_str (str): Строка даты, например "2024-03-11T02:26:18.671407"

    Возвращает:
        str: Дата в формате "11.03.2024"
    """
    from datetime import datetime

    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")
