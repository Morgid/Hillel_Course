import pytest
from hw_lesson_9 import add_three_numbers


def test_solution_1_test_1():
    assert add_three_numbers(2, 3, 5) == 10


def test_solution_1_test_2():
    assert add_three_numbers(32, 3, 5) == 40


def test_solution_1_test_3():
    assert add_three_numbers(2, 3, 5.5) == 10.5


@pytest.mark.parametrize('numb_1, numb_2, numb_3, result', [
    pytest.param(5, 2, 3, 10, id='standart'),
    pytest.param(60, -20, 0, 40, id='with minus'),
    pytest.param(5.5, 10, -5.0, 10.5, id='with float and minus')])
def test_solution_2_set_1(numb_1, numb_2, numb_3, result):
    assert add_three_numbers(numb_1, numb_2, numb_3) == result


list_test = [(5, 2, 3, 10), (60, -20, 0, 40), (5.5, 10, -5.0, 10.5)]


@pytest.mark.parametrize('numb_1, numb_2, numb_3, result', list_test)
def test_solution_3_set_1(numb_1, numb_2, numb_3, result):
    assert add_three_numbers(numb_1, numb_2, numb_3) == result
