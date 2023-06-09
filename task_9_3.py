# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

def sum_max_three():
    """
    получает сумму трёх самых дорогих покупок, записанных в полученный файл
    :return: одно число - сумма трех самых дорогих покупок
    """
    f = open("task_3.txt", 'r', encoding='utf-8')
    list_purchases = f.readlines()

    list_sums = [0]
    i = 0
    for j in range(len(list_purchases)):
        if list_purchases[j] == '\n':
            i += 1
            list_sums.append(0)
        else:
            list_sums[i] += int(list_purchases[j][:len(list_purchases[j])-1:])
    sum = 0
    for i in range(3):
        max_purchase = max(list_sums)
        sum += max_purchase
        list_sums.remove(max_purchase)
    return sum

three_most_expensive_purchases = sum_max_three()

assert three_most_expensive_purchases == 202346
