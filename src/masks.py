def get_mask_account(account: str) -> str:
    if len(account) <= 10:
        return account
    return "****" + account[-6:]


def get_mask_card_number(card_number: str) -> str:
    if len(card_number) <= 4:
        return card_number
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
