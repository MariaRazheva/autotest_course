# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

import re
# Здесь пишем код
def delete_number():
    """
    удаляет все символы-цифры из входного файла и записывает полученный текст в другой файл
    """
    f = open("test_file/task1_data.txt", 'r', encoding='utf-8')
    new_f = open("test_file/task1_answer.txt", 'w', encoding='utf-8')
    list_of_str = f.readlines()
    for i in range(len(list_of_str)):
        new_f.write(re.sub("[0-9]", "", list_of_str[i]))


delete_number()
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
