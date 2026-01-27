<<<<<<< HEAD
def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскирует номер банковской карты.

    Номер карты отображается в формате: XXXX XX** **** XXXX.
    Видны первые 6 цифр и последние 4 цифры,
    остальные символы заменены звездочками.

    :param card_number: Номер банковской карты
    :return: Замаскированный номер карты
    """
    card_number_str = str(card_number)

    # Первые 6 цифр номера карты
    first_six_digits = card_number_str[:6]

    # Последние 4 цифры номера карты
    last_four_digits = card_number_str[-4:]

    # Маска для скрытых цифр
    masked_middle = "** ****"

    return f"{first_six_digits[:4]} {first_six_digits[4:6]}{masked_middle} {last_four_digits}"


def get_mask_account(account_number: int) -> str:
    """
    Функция маскирует номер банковского счета.

    Номер счета отображается в формате: **XXXX,
    где видны только последние 4 цифры.

    :param account_number: Номер банковского счета
    :return: Замаскированный номер счета
    """
    account_number_str = str(account_number)

    return f"**{account_number_str[-4:]}"
=======
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
>>>>>>> homework_10_2
