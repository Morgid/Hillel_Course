# Ще раз конкатинація
# variable_1 = "5"
# variable_2 = "12"
# print(int(variable_1) * int(variable_2))
# print(variable_1 * int(variable_2)) # якщо стринг на число помножити, то воно відобразится стільки разів на скільки помножено
#
# variable_1 = "new"
# variable_2 = "student"
# print(variable_1,      variable_2) # , = пробіл




# #todo питання cпівбесіда Які типи данних є в Python.
# variable_1 = 10
# variable_2 = 20
# print(variable_1)
# print(variable_2)
#
# # синтаксичний цукор (зміна місцями змінних)
# variable_1, variable_2 = variable_2, variable_1
# print(variable_1)
# print(variable_2)
#
# # дорішать через математику:
# variable_1 = variable_1 + variable_2
# variable_1 = variable_2 - variable_1
# variable_2 = variable_1 - variable_2
# print(variable_1)
# print(variable_2)

# # Моножинне присвоєння
# a,b,c = 3,4,5
# print(a,b,c)

# # степінь
# print(2**3)
#
# # квадратний корінь
# print(25**0.5)

# # зарезервовані слова
# variable_1 = 999
# print = 20 # перевизначаємо функцію print
# print(variable_1 + 20)

# #float - коли в числі є крапка, то це флоат
# variable_1 = 1000000000000000000000.1 # float
# variable_2 = 999
# print(type(variable_2), variable_2)
# variable_2_float = float(variable_2)
# print(type(variable_2_float), variable_2_float)


# новий тип даних bool, в пайтоні пишется з великої літери, в інших мовах може бути з малої
# variable_true_wrong = true = не правильно, буде помилка
# Далі виводимо як тру там де є символи
# variable_true = True
# variable_false = False
# # print(int(variable_true))
# print(bool("")) # False
# print(bool(" ")) # True
# print(bool("0")) # True
# print(bool(0)) # False
# print(bool(-9)) # True
# print(bool(9)) # True
# # тип даних
# var_none = None
# print(type(var_none), var_none)
# print(bool(var_none)) # false
# матиматичні порівняння


# var_1 = 5
# var_2 = 2
# var_3 = 5 # дубль

# # >, <, >=, <=
# print(var_1 > var_2) # True
# print(var_1 < var_2) # False
# print(var_1 >= var_2) # True
# print(var_1 <= var_2) # False
# print(var_1 <= var_3) # True
# print(var_1 >= var_3) # True

# # ==, != (дорівнює, не дорівнює) порівняння по значенню
# print(var_1 == var_3) # True
# print(5 == 5.0) # True
# print(var_1 != var_3) # True

# is, not - поріняння по id
# var_1 = 5
# var_1_float = 5.0
# var_2 = 2
# var_3 = 5 # дубль
# print(id(var_1))
# print(id(var_1_float))
# print(id(var_2))
# print(id(var_3))
# # print(True)
# # print(not True)
# # print(True is True)
# # print(not(True is True))
# print(var_1 is not var_2)


# просмотреть видео !!!!!!!!!!!!!!
# variable_1 = 200
# variable_2 = 199 + 1
# print(id(variable_1))
# print(id(variable_2))
###################################

# IF
# var_1 = 5
# var_1_float = 5.0
# var_2 = 2
# var_3 = 5 # дубль

# if var_1 > var_2:
#     print("Привіт це гілка if") # виконається коли умова буде Тру
#
# else:
#     print("блок if виявився фолс тому ми в цьому блоці кода")
#
# print("text after if block")


# age = int(input("how old are you: "))

# Вкладений IF
# if age < 18:
#     print("вибачте вхід в клуб з 18 років")  # виконається коли умова буде Тру
#
# else:
#     if age >= 21:
#         print("ви можете купувати алкоголь")
#     else:
#         print("ви можете знаходитись в клубі та їсти морозиво")


# elif
# if age < 18:
#     print("вибачте вхід в клуб з 18 років")  # виконається коли умова буде Тру
#
# elif age >= 21:
#         print("ви можете купувати алкоголь")
# else:
#         print("ви можете знаходитись в клубі та їсти морозиво")
#
# password = input("please, type your password: ")
# if password == "admin":
#     print("welcome")
# else:
#     print("sorry, access deny")


# string_var = "iGor"
# print(type(string_var))
#
# print(string_var.upper()) # IGOR
# print(string_var.lower()) # igor
# print(string_var.title()) # Igor
# string_var = string_var.title() # стр зміний тип даних для збереження треба зберігати
# print(string_var)

url = "https://product_url_prod.com"
print(url)
url = url.replace("_prod", "_qa") # заміна
print(url)
url = url.replace("_", "") # видалення
print(url)

# password = input("please, type name: ")
# if password.title() == "Igor":
#     print("welcome")
# else:
#     print("sorry, access deny")