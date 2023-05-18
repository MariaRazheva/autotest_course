# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII

roman_numbers = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


def to_roman(val):
    """
    Переводит арабское число в римское
    :param val: число
    :return: строка, соответствующая римской записи входного числа
    """
    # Здесь нужно написать код
    str_val = str(val)
    list_val = []
    str_val_revers = str_val[::-1]
    roman_str_revers = ''
    for i in range(len(str_val)):
        list_val.append(int(str_val_revers[i]))
    for k in range(len(list_val)):
        j = k + 1
        if list_val[k] > 0 and list_val[k] < 4:
            roman_str_revers += list_val[k] * roman_numbers[2 * j - 2]
        if list_val[k] == 4:
            roman_str_revers += (roman_numbers[2 * j - 1] + roman_numbers[2 * j - 2])
        if list_val[k] > 4 and list_val[k] < 9:
            roman_str_revers += ((list_val[k] - 5) * roman_numbers[2 * j - 2] + roman_numbers[2 * j - 1])
        if list_val[k] == 9:
            roman_str_revers += (roman_numbers[2 * j]) + roman_numbers[2 * j - 2]
        roman_str = roman_str_revers[::-1]
    return roman_str


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']

for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
