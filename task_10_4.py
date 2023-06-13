# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


class Test:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass


    def test1(self, lead_time):
        
        assert all_division(1, 1) == 1

    def test2(self):
        with pytest.raises(ZeroDivisionError):
            all_division(1, 0)
        pass

    def test3(self):
        assert all_division(0, 1) == 0


    def test4(self):
        assert all_division(1, -1, -1) == 1



    def test5(self):
        assert all_division(256, 2, 2, 2) == 32


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division



