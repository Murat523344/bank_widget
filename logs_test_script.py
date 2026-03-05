# test_logs.py — проверка логирования

from utils import read_json, some_util_function, another_util_function
from masks import get_mask_account, get_mask_card_number

# --- utils ---
print("Проверка utils...")
read_json("test.json")  # можно создать пустой файл test.json
some_util_function(5)
another_util_function(" hello ")

# --- masks ---
print("Проверка masks...")
get_mask_account("123456789012")
get_mask_card_number("1234567890123456")

print("Проверка завершена. Смотрите логи в папке logs/")
