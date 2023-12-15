# 1) додайте requirements.txt на ваш гіт


# 3) зробіть функцію як ми робили з додаванням
# тільки замість двох чисел зробіть три числа і протестуйте її всіма трьома методами
def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result


# 2) Виберіть будь-яку помилку яка вам подобається і зробіть функцію
# яка перевіряє на цю помилку(в функції try except)
try:
    add_three_numbers(1, 41, 'd22')
except TypeError:
    print('One of number is not int')

# 4) перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює

from datetime import datetime


def func_wrapper_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print(f'Поточний час: {start}')
        result = func(*args, **kwargs)
        delta_time = datetime.now() - start
        print('Час виконання функції: ', delta_time)
        return result

    return wrapper


import time


@func_wrapper_time
def foo_1(*args, **kwargs):
    print('Функція з затримкою на 1 секунду')
    time.sleep(1)


@func_wrapper_time
def foo_2(*args, **kwargs):
    print('Функція з затримкою на 2 секунди')
    time.sleep(2)


foo_1()
foo_2()
