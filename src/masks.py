def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.
    """
    if not card_number or len(card_number) < 16:
        return card_number

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.
    """
    if len(account_number) < 20:
        return account_number

    return f"****{account_number[-6:]}"
