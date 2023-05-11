# Напишите функцию, которая принимает кортеж num_tuple из 10 цифр num_tuple,
# и возвращает строку этих чисел в виде номера телефона str_phone.
# Например (Ввод --> Вывод) :
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  => "(123) 456-7890"

def create_phone_number(num_tuple):
    """
    Получить строку номера телефона, состоящую из цифр, поданных на вход
    :param num_tuple: кортеж цифр
    :return: строка в формате номера телефона
    """
    str_of_number = ''
    for i in range(len(num_tuple)):
        str_of_number += str(num_tuple[i])
    str_phone = '(' + str_of_number[0:3] + ') ' + str_of_number[3:6] + '-' + str_of_number[6:]
    print(str_phone)
    return str_phone


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

data = [
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 2, 3, 0, 5, 6, 0, 8, 9, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
]

test_data = [
    "(123) 456-7890", "(111) 111-1111", "(023) 056-0890", "(000) 000-0000"
]

for i, d in enumerate(data):
    assert create_phone_number(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')