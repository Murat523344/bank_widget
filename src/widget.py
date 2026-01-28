from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account: str, card_number: str) -> tuple[str, str]:
    """
    Маскирует номер счета и номер карты.
    """
    return get_mask_account(account), get_mask_card_number(card_number)


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата 'YYYY-MM-DD' в 'DD.MM.YYYY'.
    """
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return date_str
