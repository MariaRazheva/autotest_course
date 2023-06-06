# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

set_numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# Здесь пишем код
def delete_number():
    f = open("test_file/task1_data.txt", 'r', encoding='utf-8')
    new_f = open("test_file/task1_answer.txt", 'w', encoding='utf-8')
    list_of_str = f.readlines()
    for i in range(len(list_of_str)):
        for j in range(len(list_of_str[i])):
            if not list_of_str[i][j] in set_numbers:
                new_f.write(list_of_str[i][j])


delete_number()
# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')