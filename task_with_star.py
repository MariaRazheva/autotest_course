# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    """
    Получить число, максимальное из возможных, удовлетворяющее условиям:
    1) делимость на 3
    2) отличие на 1 цифру от входного
    3) количество цифр как у входного
    :param num: число
    :return: число, удовлетворяющее указанным выше условиям
    """
    lst_num = make_lst_of_int(num)
    copy_lst_num = list(lst_num)
    new_num = 0
    for i in range(len(lst_num)):
        for j in range(9, 6, -1):
            copy_lst_num[i] = j
            print(copy_lst_num, 'i', i, 'j', j)
            if (sum(copy_lst_num) % 3 == 0) and (new_num < make_int_of_lst(copy_lst_num)) and (
                    make_int_of_lst(copy_lst_num) != num):
                new_num = make_int_of_lst(copy_lst_num)
            copy_lst_num = list(lst_num)
    return new_num


def make_lst_of_int(num):
     """
    получает список цифр числа (по порядку вхождения слева направо)
    :param num: число
    :return: список его цифр
    """
    str_num = str(num)
    lst_num = [int(str_num[i]) for i in range(len(str_num))]
    return lst_num


def make_int_of_lst(lst):
    """
    Получить одно число из списка цифр (по порядку слева направо)
    :param lst: список цифр
    :return: число
    """
    str_of_lst = ''
    for i in range(len(lst)):
        str_of_lst += str(lst[i])
    # print(int(str_of_lst))
    return int(str_of_lst)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]

for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
