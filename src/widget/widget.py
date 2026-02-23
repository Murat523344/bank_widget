from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def get_date(date_str: str) -> str:
    date_str = date_str.replace("/", "-")
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")


def mask_account_card(value: str) -> str:
    if len(value) > 16:
        return get_mask_account(value)
    return get_mask_card_number(value)


def render_widget() -> str:
    return "Widget rendered successfully"
