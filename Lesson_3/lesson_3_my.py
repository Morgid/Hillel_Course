# or, and

# print(True or True)
# print(True or False)
# print(False or False)
# print(True and False)
# print(False and True)
#
# print(True or True)
# print(True or True)


# # форматування коду в пейчармі ctrl+alt+l
# a = 23 + 99
# print(a)

# round
# print(0.0001 + 0.0002) # багато 000000
# print((1 + 2)/10000) # вихід 1
# # import decimal # імпортування нового типу даних який працює з флоат без помилок
# a = (0.0001 + 0.0002)
# print(a)
# a = round(a, 2) # округляє, а цифра вказує на кількість знаків взагалом
# print(a)

# # in str
# string_a = 'aadjjjdhhsjh sjjdhs  jsj'
# print('jsj ' in string_a)


# f string
# name = 'Ivan'
# age = 32
# print(f'Hi {name} you are {age} old')
#
# print(f'Hi {name} you are {age +32} old')
# print(f"{name=}")
# new_string = (f'Hi {name} you are {age +32} old')
# print(new_string)


# len# рахує кількість символів або єлементів в стрічці, повертає інтежер
# print(len(new_string))

# strip, lstrip, rstrip
# my_string = '++++ abdc +++ sadasf+++'
# print(my_string.strip("+"))  #abdc +++ sadasf
# print(my_string.lstrip("+")) #abdc +++ sadasf+++
# print(my_string.rstrip("+")) #++++ abdc +++ sadasf
# print(my_string.strip("+"))


#  count, isdigit, find, isalpha
# print((my_string.count('+'))) # кількість елементів

# var_1 = "999"
# var_2 = "text"
# print(var_1.isdigit())
# print(var_1.isalpha())
# number_a = input()
# number_b = input()
#
# if number_a.isdigit() and number_b.isdigit():
#     print((int(number_a) + int(number_b))*3)
# else:
#     print("Ми працюємо тільки з цілими числами")

# зріз в стр find
# string_a = "Hello, how you doin? What a day!"
# index_1 = 10
# print(string_a[0]) # буде перший символ
# print(string_a[4]) # буде 4й символ
# print(string_a[0:4]) # з першого по четвертий символ
# print(string_a[4:7])
# print(string_a[0:index_1]) # зі змінною
# print(string_a[:10]) # з початку строки по 10 символ
# print(string_a[10:])
# print(string_a[:]) # всю строку
# print(string_a[:10000])
# print(string_a[:-1]) # з кінця
# print(string_a[:-10])
# print(string_a[-5:-1])
# print(string_a[-5:])
# print(string_a[-0:4])
# print(string_a[0:9:2]) # 2= через 1 буде виводить
# print(string_a[len(string_a) // 2:]) # з середини текста
# і до кінця (лен - рахує всі символі, переводить до інт, ділить на 2 = середина

# list списки
# list_a = [] # emty list
# print(type(list_a), list_a)
# list_b = [1, 23.0, 1, 1, None, True, "rertg", [2,3,555,"hjj0"]]
# print(type(list_b), list_b)
# print(list_b[-2].upper())
# print(list_b[-1][1])

# list_a = [23,33,454]
# list_b = list_a
# print(id(list_a), id(list_b), sep='\n', end='\nце все\n')
#
# print(list_a)
# print(list_b)
# list_a.append(100) # додали ще число в ліст, так як а і б однакові, то додало і туда і туда
# print(list_a)
# print(list_b)
#
# del_element = list_a.pop() # можем і не зберігати
# print(list_a)
# print(list_b)
# print(type(del_element), del_element)

# list_a = [23,33,454]
# list_b = list_a [:] # 1 варіант
# print(list_a)
# print(list_b)
# list_a.append(200)
# print(list_a)
# print(list_b)
# second variant
# import copy
# list_c = [23,33,454]
# list_d = copy.deepcopy(list_c)
# print(list_c)
# print(list_d)
# list_c.append(200)
# print(list_c)
# print(list_d)

# list_a = [12, 10, 4, 12, 11] # список балів в групі
# print(sum(list_a)/len(list_a)) # середній бал в руппі

# string_a = '345 567 44'
# list_of_number  = string_a.split()
# print(type(list_of_number), list_of_number)
# print(list_of_number[1])