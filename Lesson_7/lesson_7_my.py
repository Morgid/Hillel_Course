#namespace BGLN (built in, global, local, non-local)
#
# point_b = 77
#
# def foo(age: int, username: str = "default)") -> str:
#     point_a = 999 #local
#     string = f"{username}, {age}"
#     print(point_b)
#
#     return string
# print(point_b)

# # Можна використовувати одну назву змінних в різних функціях
# d = 32
#
# def foo(d):
#     d= d+32
#     print(d)
#     return "no None"
#
# print(d) # 32
# print((foo(d=10))) # 42, no None
# # print(d) # 32


# [13]
# [13, 15]
# [13, 15, 34] - результат. Не можна списком
# def foo(arg_a: str, list_1: list=[]) -> str:
#     list_1.append(arg_a)
#     return list_1
#
# print(foo(13))
# print(foo(15))
# print(foo(34))



# [13]
# [15]
# [34]
# def foo(arg_a: str, list_1=tuple([])) -> str:
#     list_1= list(list_1)
#     list_1.append(arg_a)
#     return list_1
#
# print(foo(13))
# print(foo(15))
# print(foo(34))


# безимянна змінна
# Lambda, анонімна

# calc_dict = {
#     "+":lambda a, b: a+b,
#     "*":lambda a, b: a*b,
#     "/":lambda a, b: a/b,
#     "-":lambda a, b: a-b
# }
# def concatenete(string_a: str, string_b: str) -> str:
#     result = string_b+string_a
#     return result
# print(concatenete(string_a="ololo", string_b="GHH"))
# #
# print("Lesson_7")
# print(calc_dict["+"](a=199, b=1))
# print(calc_dict["*"](a=199, b=2))

#sorted
# list_1=[34,11,3333,456,12,-100, 11,99]
# list_2=['oloo', 'fdfd', 'gggg', 'dffffff']
# print(sorted(list_1)) # від меншого до більшого
# print(sorted(list_1, reverse=True)) # з більшлго до меншого
# print(sorted(list_2)) # по алфавіту
# print(sorted(list_2, key=len)) # по символьно
# print(sorted(list_2, key=lambda a: a[-1])) # по останній букві
# print(sorted(list_1, key=lambda a: a%2))


# *args, **kwargs
# a,b,*c = [2,3,4,4,4,6,7] # запишемо все що не присвоєно в с як лист
# print(a,b,c)


# def foo(*args) -> int|float:
#     age, height, *list_2 = args
#     if list_2 != []:
#         for i in list_2:
#             print(i)
#     print(age, height)
#     print(list_2)
#     print(type(args))
#     list_1 = args
#     return  sum(list_1)
#
# print(foo(34,43,45,2,2,2,))
# print(foo(34,43))

# def foo(*args) -> int|float:
#     age, height, *list_2 = args
#     if list_2: # те саме що і !=[]
#         for i in list_2:
#             print(i)
#     print(age, height)
#     print(list_2)
#     print(type(args))
#     list_1 = args
#     return  sum(list_1)
#
# print(foo(34,43,45,2,2,2,))
# print(foo(34,43))


# def foo(*args,**kwargs) -> int|float:   # ???????????
#     dict_1, dict_2 = kwargs
#     print()
#
#
# print(foo(33, a=34, c=121212, b=45))
# # print(foo(34,43))
# dict_a = {33:32}
# dict_b = {10:100}


# Штука з бібліотеками, буде повідомлення... треба скрипт для Вінди
# import os
# import time
#
# while True:
#     command = f"""osascript -e 'display notification' "прйшло 10 секунд" """
#     os.system(command)
#     time.sleep(10)


# YAGNI - вам це не знадобиться, патерн (You Aren`t Going to Need It)

# ascii, ord VS chr
# print(ascii("t"))
# print(ascii("c")) # Англ с
# print(ascii("с")) # Укр с
# print(ascii("ї"))
# print(ascii(" "))
#
# print(ord("F")) # повертає цифрове значення
# print(ord("f"))
# print(ord(" "))
#
# print(chr(102)) # повертає букви
# print(chr(72))
print(chr(32)) # пробіл

