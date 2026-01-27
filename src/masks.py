def get_mask_account(account: str) -> str:
    """
    Маскирует номер счета, оставляя последние 6 цифр видимыми.
    Пример: '12345678901234567890' -> '****567890'
    """
    if len(account) <= 10:
        return account
    return "****" + account[-6:]


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате тестов.
    Пример: '1234567890123456' -> '1234 56** **** 3456'
    """
    if len(card_number) <= 4:
        return card_number
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
