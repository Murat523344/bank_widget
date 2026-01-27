from src.widget.widget import mask_account_card, get_date

# Проверка маски карт и счетов
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))

# Проверка преобразования дат
print(get_date("2024-03-11T02:26:18.671407"))
print(get_date("2018-07-11T10:30:00"))
