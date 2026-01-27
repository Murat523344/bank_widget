from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.

    Функция принимает строку с названием карты или счета и номером,
    например: "Visa Platinum 7000792289606361" или "Счет 73654108430135874305".
    Возвращает строку с замаскированным номером, используя функции
    get_mask_card_number и get_mask_account.

    :param info: Строка с типом карты/счета и номером
    :return: Строка с замаскированным номером
    """
    parts = info.rsplit(' ', 1)  # разбиваем только последний пробел
    name = parts[0]
    number = parts[1]

    if number.isdigit():
        if name.lower().startswith("счет"):
            masked_number = get_mask_account(int(number))
        else:
            masked_number = get_mask_card_number(int(number))
    else:
        masked_number = number  # если что-то не число, возвращаем как есть

    return f"{name} {masked_number}"

from datetime import datetime

def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой из формата ISO 8601
    ("YYYY-MM-DDTHH:MM:SS.microseconds") в формат "ДД.ММ.ГГГГ".

    :param date_str: Строка с датой в формате ISO 8601
    :return: Строка с датой в формате "ДД.MM.ГГГГ"
    """
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return date_str  # если формат некорректный, возвращаем как есть
