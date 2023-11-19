# В кінці уоду треба ставити пробіл (пусту стрічку?) для компілятора
# гіта та POSIX

# пів урока пропустив - дивись запис!!


# set - приймає тільки не зміні типи даних.
# Змінний тип даих. SET - mutable, FROZENSET -immutable


# Dir Можна попачити які методи є в цих списках, таплах, сетах
# list_a = [1,1,1,2,2,2]
# tuple_a = (1,1,1,3,3,3)
# set_a = {1,1,1,1,3,3,3}

# # sizeof - для розуміння скільки пам'яті використовує
# print(list_a.__sizeof__())
# print(tuple_a.__sizeof__())
# print(set_a.__sizeof__())
#
# print(dir(list_a))
# print(dir(tuple_a))
# print(dir(set_a))


# Цикл в циклі
# Таблиця множення
# 1 приклад
# for i in range(1,10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i*j}")

# 2 приклад
# for i in range(2, 10):
#     for j in range(2, 10):
#         print(f"{i}*{j}={i*j}", end="")
#     print()

# KISS - keep it simple - не намагайтеся ускладнювати код


# DICT
# dict_a = {} #dict
#dict_a = set() # set
# dict_a = 4,3 # tuple
# dict_a, d = 4, 6 # int
# print(dict_a, type(dict_a))

# Однакові
# dict_1 = {}
# dict_2 = dict()
#
# print(dict_1, type(dict_1))
# print(dict_2, type(dict_2))


# dict_1 = {}
# dict_2 = dict()
# dict_3 = dict(city="Odesa", village = "Myrne")
#
# print(dict_1, type(dict_1))
# print(dict_2, type(dict_2))
# print(dict_3, type(dict_3))


# dict_1 = {}
# dict_2 = dict()
# dict_3 = dict(city="Odesa", village = "Myrne")
# dict_4 = dict([(1, 2), ("key", "value")])
#
# print(dict_1, type(dict_1))
# print(dict_2, type(dict_2))
# print(dict_3, type(dict_3))
# print(dict_4, type(dict_4))


# dict_1 = {}
# dict_2 = dict()
# dict_3 = dict(city="Odesa", village = "Myrne")
# dict_4 = dict([(1, 2), ("key", "value")])
# dict_5 = dict.fromkeys([3,4,5], "default")
#
# print(dict_1, type(dict_1))
# print(dict_2, type(dict_2))
# print(dict_3, type(dict_3))
# print(dict_4, type(dict_4))
# print(dict_5, type(dict_5))

# # hash - може бути використаний тільки для незмінних типів даних
# list_a = "[]"
# print(hash(list_a))


# Запис словника (6 - найпоширеніший)
# dict_1 = {}
# dict_2 = dict()
# dict_3 = dict(city="Odesa", village = "Myrne")
# dict_4 = dict([(1, 2), ("key", "value")])
# dict_5 = dict.fromkeys([3,4,5], "default")
# dict_6 = {"Ololo": ["AQA", "python"], "Dmytro":["DevOps", "bash"]}
#
# print(dict_1, type(dict_1))
# print(dict_2, type(dict_2))
# print(dict_3, type(dict_3))
# print(dict_4, type(dict_4))
# print(dict_5, type(dict_5))
# print(dict_6, type(dict_6))


# Вивід
# dict_6 = {"Ololo": ["AQA", "python"], "Dmytro":["DevOps", "bash"]}
# print(dict_6["Ololo"])

# dict_6 = {"Ololo": ["AQA", "python"], "Dmytro":["DevOps", "bash"]}
# print(dict_6["Ololo"]) # один вивід
# print(dict_6) # весь список
# print(dict_6["Ololo"].append('C++++')) # Додавання в значення
# print(dict_6)
#
# dict_6["Ololo"] = ["PM"] # перезапис
# print(dict_6)
#
# dict_6["Dmytro"][1] = "C++" # зміна одного із значень
# print(dict_6)


