# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

# Здесь пишем код
def letter_stat(our_str):
    """
    Возвращает словарь, где ключи - буквы заданного слова, а значения - количество вхождений буквы в данное слово
    :param our_str: исходное слово
    :return: словарь соответствия буквы количеству её вхождений в слово
    """
    letters_set = set()
    letters_dict = {}
    for i in range(len(our_str)):
        if our_str[i] in letters_set:
            letters_dict[our_str[i]] += 1
        else:
            letters_dict[our_str[i]] = 1
            letters_set.add(our_str[i])
    return letters_dict


class PersonInfo:

    def __init__(self, name, age, *args):
            """
        Инициализирует объект полученными данными - имя, возраст, подразделения
        :param name: строка с именем сотрудника
        :param age: число - возраст сотрудника
        :param args: подразделения, в которых состоит сотрудник от заглавного до конечного
        """
        self.name = name
        self.age = age
        self.way = args

    def short_name(self):
            """
        Возвращает строку формата "Фамилия И." данного сотрудника
        :return: строка "Фамилия И."
        """
        name = self.name.split()[1];
        surname_first_letter = self.name.split()[0][0]
        string_short_name = name + ' ' + surname_first_letter + '.'
        return string_short_name

    def path_deps(self):
            """
        Возвращает строку пути от головного до конечного подразделения с разделителем ' --> '
        :return: строка пути
        """
        path = ""
        for i in range(len(self.way)):
            path += self.way[i]
            if i < len(self.way) - 1:
                path += ' --> '
        return path

    def new_salary(self):
            """
        Возвращает будущую зарплату посчитанную как произведение 1337, возраста и количества вхождений трех самых часто встречающихся букв в подразделениях сотрудника 
        :return: число - зарплата, посчитанная по описанной формуле
        """
        path = ""
        for i in range(len(self.way)):
            path += self.way[i]
        new_dict = letter_stat(path)
        new_list = []
        counter = 0
        for counter in range(3):
            max_val = max(new_dict.values())
            for key in new_dict.keys():
                if new_dict[key] == max_val:
                    key_to_delete = key
            new_list.append(max_val)
            new_dict.pop(key_to_delete)
        koeff_letters = new_list[0] + new_list[1] + new_list[2]
        return 1337 * self.age * koeff_letters



# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]

test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
