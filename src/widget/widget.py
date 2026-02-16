from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def get_date(date_str: str) -> str:
    """
    Преобразует дату из ISO или с '/' в формат "ДД.MM.ГГГГ".
    """
    date_str = date_str.replace("/", "-")
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")


def mask_account_card(value: str) -> str:
    """
    Маскирует счет или карту в соответствии с тестами.
    Если длина > 16 - счет, иначе карта.
    """
    if len(value) > 16:
        return get_mask_account(value)
    return get_mask_card_number(value)
