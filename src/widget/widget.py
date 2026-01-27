

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

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """
    Маскирует номер карты или счета.
    """
    if not card_info:
        return ""

    # если передали только цифры
    if card_info.isdigit():
        if len(card_info) == 16:
            return get_mask_card_number(card_info)
        if len(card_info) == 20:
            return get_mask_account(card_info)
        return card_info

    parts = card_info.rsplit(" ", 1)
    if len(parts) != 2:
        return card_info

    name, number = parts

    if number.isdigit():
        if len(number) == 16:
            return f"{name} {get_mask_card_number(number)}"
        if len(number) == 20:
            return f"{name} {get_mask_account(number)}"

    return card_info



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

