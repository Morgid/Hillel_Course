from hw_lesson_7 import sorting_by_increase
from hw_lesson_7 import sorting_by_decrease
from hw_lesson_7 import sorting_by_letters


def test_sorting_by_increase() -> list:
    assert sorting_by_increase() == [-777, -66, -5, 0, 1, 2, 3, 4, 12, 22, 55.4, 66, 66.6, 400]


def test_sorting_by_decrease() -> list:
    assert sorting_by_decrease() == [400, 66.6, 66, 55.4, 22, 12, 4, 3, 2, 1, 0, -5, -66, -777]


def test_sorting_by_letters() -> list:
    assert sorting_by_letters() == ['Є', 'ця', 'лиш', 'одна', 'фраза', 'роботи', 'перевірки', 'сортування',
                                    'функцією!!!']
