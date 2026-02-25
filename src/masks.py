import logging

# --- Логгер для модуля masks ---
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_account(account: str) -> str:
    """
    Маскирует банковский счет: если длина > 10, показывает только последние 6 цифр.
    """
    try:
        if len(account) <= 10:
            logger.debug(f"get_mask_account({account}) -> {account} (не маскировалось)")
            return account
        masked = "****" + account[-6:]
        logger.debug(f"get_mask_account({account}) -> {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировании счета {account}: {e}")
        raise


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты: показывает первые 4 и последние 4 цифры, остальное маскируется.
    """
    try:
        if len(card_number) <= 4:
            logger.debug(f"get_mask_card_number({card_number}) -> {card_number} (не маскировалось)")
            return card_number
        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.debug(f"get_mask_card_number({card_number}) -> {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировании карты {card_number}: {e}")
        raise
