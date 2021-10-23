import random
import datetime
import os

# Список символов
ARRAY_SYMBOLS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
                 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
                 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '@', '!', '#', '$',
                 '%', '=', '&']

# Получение количества символов в пароле
CONST_COUNT_SYMBOLS = 6

custom_count_symbols = int(input("Введите количество символов в пароле: "))

if custom_count_symbols > 0:
    count_symbols = custom_count_symbols
else:
    count_symbols = CONST_COUNT_SYMBOLS

count_variant = len(ARRAY_SYMBOLS) ** count_symbols


# Функция случайных символов
def random_symbols():
    return ARRAY_SYMBOLS[random.randint(0, len(ARRAY_SYMBOLS) - 1)]


print(f'Версия программы: v0.0.1')
print(f'Количество доступных символов: {len(ARRAY_SYMBOLS)}')
print(f'Доступные символы: {ARRAY_SYMBOLS}')
print(f'Количество возможных комбинаций: {count_variant}')

# Генерируем уникальный пароль.
password = ''
for i in range(0, count_symbols):
    password = password + f'{random_symbols()}'

print(f'Сгенерированный пароль: {password}')

text_datetime = f'{datetime.datetime.now()}'
symbols_replace = ['-', ' ', ':', '.']
file_name = ''
for s in text_datetime:
    is_write = True
    for sr in symbols_replace:
        if s == sr:
            file_name += '_'
            is_write = False
    if is_write:
        file_name += s

if not os.path.exists('passwords'):
    os.mkdir('passwords')

# Запись пароля в файл.
with open(f'passwords/{file_name}_password.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password}'))

input()