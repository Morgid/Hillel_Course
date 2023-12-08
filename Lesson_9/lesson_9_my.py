# # docstring - це опис функції
# def foo(numbe_1: int, number_2: int) -> int:
#     """
#     add two numbers
#     :param numbe_1 int: first number
#     :param number_2 int: srcond number
#     :return int: result add two numbers
#     """
#     result = numbe_1 + number_2
#     return result

# use default only when your func need it. Не юзаємо інпут в оголошенні функціі, та краще дефолтні значення не треба


# ENV add reqirentment
# - в відео лекції

# Exceptions

# print(40/0) # ZeroDivisionError: division by zero
# try:
#     print(40/0)
# except:
#     print("Не можна ділити на 0") # так ловляться всі ексепшени (ловля Покемонів)

# try:
#     print(40/0) # відпрацює першим, якщо закоментувати 40/0 то буде наступний еррор
#     print(int("hjhjhj")) # ValueError: invalid literal for int() with base 10: 'hjhjhj'
# except ZeroDivisionError:
#     print("Не можна ділити на 0")

# # value_1 = "0" # Не можна ділити на 0
# value_1 = "hjkhjk" # Не цифра
# try:
#     print(40/int(value_1))
# except ZeroDivisionError:
#     print("Не можна ділити на 0")
# except ValueError:
#     print("Не цифра")

# # print(40/0) # ZeroDivisionError: division by zero
# try:
#     print(40/0)
# except Exception as e:
#     print("Не можна ділити на 0") # так ловляться всі ексепшени (ловля Покемонів)
#     print(f" we get error -> {e} <- ") # впише в змінну е помилку

# # Pytest parametrize
# def add_two_nummbers(number_1: int|float, number_2: int|float) -> int|float:
#     result  = number_1 +number_2
#     return  result
#
#
# tuple_1 = (1,2,3)
# print(type(tuple_1), tuple_1)
#
# tuple_2 = 1,2,3
# print(type(tuple_2), tuple_2)


# Decorator
# def func_wrapper(func):
#     def wrapper(*arg, **kwarg):
#         print("before")
#         result = func(*arg, **kwarg)
#         print("after")
#         return result
#     return wrapper

# @func_wrapper
# def bar(*arg, **kwarg):
#     print("Hello", arg, kwarg)


# wrapped_func = func_wrapper(bar)
# wrapped_func()

# # Випадок 2
# @func_wrapper
# def bar_1(*arg, **kwarg):
#     print("Hello", arg, kwarg)
#
# @func_wrapper
# def bar_2(*arg, **kwarg):
#     print("Hello", arg, kwarg)
#
# bar_1(111)
# bar_2(222)

# #Про час декоратор
#
# from datetime import datetime


# def func_wrapper_time(func):
#     def wrapper(*arg, **kwarg):
#         start = datetime.now()
#         print("start")
#         result = func(*arg, **kwarg)
#         delta_time = datetime.now() - start
#         print("Час виконання функції ось такий: ", delta_time)
#         return result
#     return wrapper
#
# import time
# @func_wrapper_time
# def foo_1(*arg, **kwarg):
#     print("foo_1")
#     time.sleep(1)
#
#
# @func_wrapper_time
# def foo_2(*arg, **kwarg):
#     print(foo_2.__name__)
#     time.sleep(2)
#
# foo_1()
# foo_2()

