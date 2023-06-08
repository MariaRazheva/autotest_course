# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    n = 0
    while n == 0:
        list_roman = string.ascii_letters
        len_1 = random.randint(1, 15)
        len_2 = random.randint(1, 15)
        random_first = ''
        for i in range(len_1):
            random_first += random.choice(list_roman)
        random_first += ' '
        for i in range(len_2):
            random_first += random.choice(list_roman)
        yield random_first


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# Здесь пишем код