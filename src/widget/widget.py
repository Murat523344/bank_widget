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
    Преобразует дату в формат DD.MM.YYYY
    """
    if not date_str:
        return ""

    date_str = date_str.replace("/", "-")
    parts = date_str.split("-")

    if len(parts) != 3:
        return date_str

    year, month, day = parts
    return f"{day}.{month}.{year}"
