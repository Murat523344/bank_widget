def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя последние 6 цифр видимыми.
    Пример: '12345678901234567890' -> '****567890'
    """
    if len(account_number) < 20:
        return account_number
    return f"****{account_number[-6:]}"


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.
    Пример: '1234567890123456' -> '1234 56** **** 3456'
    """
    if not card_number or len(card_number) < 16:
        return card_number
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
