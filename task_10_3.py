# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните


import pytest


@pytest.mark.parametrize('in_data, out', [pytest.param((1, 1), 1, marks=pytest.mark.skip), ((1, 0), pytest.raises(ZeroDivisionError)), pytest.param((0, 1), 0, marks=pytest.mark.smoke), ((1, -1, -1), 1), ((256, 2, 2, 2), 32)])
def test_all_division(in_data, out):
    if not pytest.raises(ZeroDivisionError):
        assert all_division(*in_data) == out



#def test2():
    # #assert all_division(1, 0) == ZeroDivisionError
    # with pytest.raises(ZeroDivisionError):
    #     all_division(1, 0)


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    print(division)
    return division
