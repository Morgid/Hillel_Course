# # перевернути, починаємо з кінця йдемо до початку
# word = "стілець"
# l_word = [2,2,0]
# print(word[::-1])
# import math

# #  extend - додавання списку в списук (показати на стрічці різницю)
# list_a = [1,2]
# list_b = ['sadsa','asds']
#
# list_a.append('привіт')
# list_b.extend('привіт')
# print(list_a)
# print(list_b)
#

# remove - видалення елемента по конкретному знченню
# list_product = [1, "sdfds",23, 33]
# print(list_product)
# list_product.remove('sdfds') # маємо знати що видаляти
# print(list_product)
#  Видаляє тільки перший знайдений єлемент, і ніяк по іншому

# import math
# print(math.ceil(0.00001))  # округлює до більшого
# print(math.floor(1.9999))  # округлює до меншого
# print(math.ceil(0.0001) == math.floor(1.999))

# # Константи
# person_age = 10
# PENSION = 60 # константи пишуться капсом, бо вона незмінна

# for in (brek, continue), зміна списку на ходу
# for i in [1,2,34,]:
#     print(i)
#     input()  # покроково, в кожен інпут буде записано
# print('finish')

# for i in "Привіт":
#     print(i.upper())
# print('finish')

# list_a = [1772,True,612,"ghGGhg",1442,1,2222,3,23,2,32,23]
# new_number_list = []
# print(list_a)
# for element in list_a:
#     element = str(element)
#     if element.isdigit():
#
#         new_number_list.append(int(element)/100)
#     elif element.isalpha():
#         print(f'Ваш елемент = {element}')
#
# print(new_number_list)


# Додаэмо isinstance для перевірки elemet на стр чи інт
# list_a = [1772,True,61.2,"ghGGhg",1442,1,22.22,3,23,2,32,23]
# new_number_list = []
# print(list_a)
# for element in list_a:
#     if isinstance(element, (int, float)):
#         new_number_list.append(int(element)/100)
#     elif isinstance(element, str):
#         print(f'Ваш елемент = {element}')
#
# print(new_number_list)


# list_a = [1772,True,61.2,"ghGGhg",1442,1,22.22,3,False, 23,2,32,23]
# new_number_list = []
# print(list_a)
# for element in list_a:
#     element = str(element)
#     if element.isdigit():
#
#         new_number_list.append(int(element)/100)
#     elif element.isalpha():
#         if element == "True":
#             continue # пропускає ітерацію і йде до наступного елементу
#         elif element == "False":
#             break # Обірве цикл повністю
#         print(f'Ваш елемент = {element}')
#
# print(new_number_list)




# Кортеж
# todo Чим відрізняється tuple від list
# list_i = [3,4,5]
# tuple_i = (3,4,5)
# for i in tuple_i:
#     print(i)
# tuple_2 = tuple(list_i)
# print(tuple_i, type(tuple_i))
# print(tuple_2, type(tuple_2))
# list_b = list_i
# list_b = list(tuple(list_i))
# print(id(list_i))
# print(id(tuple_2))


# # цикл while
# import time
#
# while True: # так ніколи не робіть,бо буде по кругу завжди
#     time.sleep(1)
#     print(1)


# n = 0
# while n < 12:
#     n += 1 # equal n = n+1
#     if n in (4,5,6): # n == 4, n == 5 ...
#         continue
#     print(f'{n} = {n**2}')
#     n += 1 # equal n = n+1

# plus element ;
# new_string = ";".join("Hello Ololo")
# print(new_string)

# new_string = ";".join("Hello Ololo")
# print(new_string)
# list_a = ['12', 'fghfh', 'shmpan']
# string_from_list = "OLOLO".join(list_a)
# print(string_from_list)


# name = "Serg"
# mid_name = "Olo"
# balance = 1500000
#
# # text = """Hello {0} {1}, balance is {2} uah""".format(name, mid_name, balance)
# # print(text)

# Патерн DRY = don`t repeat your self


