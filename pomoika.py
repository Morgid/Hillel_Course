# # Візьміть дві задачі з попередніх уроків, перша легка по вирішенню(декілька стрічок),
# # друга більш складна і перепишіть їх на функції. Памятайте про Атамарність та god object.
# # Там де написано що користувач має щось ввести то перероблюємо на функція приймає.
# # Подивіться може можна за допомогою функції спростити код. В домашку вставте будь ласка опис задачі
# # (далі(один з наступних уроків) буде домашка вашу домашку покрити тестами, але ми трохи поміняємо варіанти).
#
#
# # Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно).
# # (так як робили на уроці). Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
# #
# # Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# # (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.
#
#
# def need_table():
#     need_table = input("Яку табличку ви хочете побачити? (+, -, /, *): ")
#
#     if need_table in table_dict:
#         display_table(need_table)
#     else:
#         print("Будь ласка, виберіть таблицю ще раз")
#
# def multiplication():
#     multi_list = []
#     for i in range(2, 10):
#         for j in range(1, 10):
#             multi_list.append(f"{i} * {j} = {i * j}")
#     return multi_list
#
# def subtraction():
#     substract_list = []
#     for i in range(2, 10):
#         for j in range(1, 10):
#             substract_list.append(f"{i} / {j} = {round((i / j), 2)}")
#     return substract_list
#
# def division():
#     division_list = []
#     for i in range(2, 10):
#         for j in range(1, 10):
#             division_list.append(f"{i} - {j} = {i - j}")
#     return division_list
#
# def addition():
#     addition_list = []
#     for i in range(2, 10):
#         for j in range(1, 10):
#             addition_list.append(f"{i} + {j} = {i + j}")
#     return addition_list
#
# table_dict = {
#     "+": [addition()],
#     "-": [division()],
#     "/": [subtraction()],
#     "*": [multiplication()]}
#
#
# def display_table(need_table):
#     if need_table == "+":
#         print("Таблиця додавання:")
#         print(table_dict.get("+"))
#     elif need_table == "-":
#         print("Таблиця віднімання:")
#         print(table_dict.get("-"))
#     elif need_table == "/":
#         print("Таблиця ділення:")
#         print(table_dict.get("/"))
#     elif need_table == "*":
#         print("Таблиця множення:")
#         print(table_dict.get("*"))
#     else:
#         print("Будь ласка, виберіть таблицю ще раз")
#         return
#
# need_table()
# def recursion(i: int) -> int:
#     if i <= 1:
#         return 1
#     return i + recursion(i - 1)


# print(recursion(4))
#
# list_2 = ["Flake8==6.1.0",
# "pytest==7.1.2",
# "pytest-xdist===3.5.0",
# "requests==2.31.0"]
#
# print(sorted(list_2))


# version = '12.23.1.33'
# rise_version = '12.23.1.33d'








# hex_list = version.split('.')
# rise_hex_list = rise_version.split('.')
# print(hex_list)
# print(rise_hex_list)


# print(chek_last_hex('12.23.1.33', '12.23.1.37'))

# def chec_version(version):
#     version_list = version.split('.')
#     for elemets in version_list:
#         if isinstance(elemets, str):
#             last_hex = elemets
#         else:
#             last_hex = int(version.split('.')[-1])
#     return last_hex
#
# def chec_version_rise(rise_version):
#     version_list = rise_version.split('.')
#     for elemets in version_list:
#         if isinstance(elemets, str):
#             last_hex_rise = elemets
#         else:
#             last_hex_rise = int(version.split('.')[-1])
#     return last_hex_rise



    # last_hex = int(version.split('.')[-1])
    # rise_last_hex = int(rise_version.split('.')[-1])
    # result = rise_last_hex - last_hex
    # if result <= 0:
    #     print(f'Актуальна версія {version}')
    # else:
    #     print(f'Нова версія: {rise_version}')
    # return result

    # rise_list = rise_version.split('.')
    # for elemets_rise in rise_version:
    #     if isinstance(elemets_rise, str):
    #         last_hex_rise = elemets_rise
    #
    #
    # for elemets in version_list:
    #     if isinstance(elemets, str):
    #         last_hex = elemets


# print(chec_version_rise('12.23.1.33d'))



# last_hex = version.split('.')[-1]
# rise_last_hex = rise_version.split('.')[-1]
# if version.split('.')[-1] and rise_last_hex.isdigit():
#     if int(last_hex) - int(rise_last_hex) == 0:
#     print("Версії однакові")
#         else
# else
# result = int(last_hex) - int(rise_last_hex)
# print(result)


# for elements in version.split('.'):
#     result = elements+elements
#     print(result)
# print((str(version.split('.')[-1]))+(str(rise_version.split('.')[-1])))


# def compare_versions(version1, version2):
#     # Разделяем версии на компоненты
#     components1 = version1.split('.')
#     components2 = version2.split('.')
#
#     # Выполняем сравнение компонентов
#     for c1, c2 in zip(components1, components2):
#         if c1.isdigit() and c2.isdigit():
#             if int(c1) > int(c2):
#                 return f'{version1} новее чем {version2}'
#             elif int(c1) < int(c2):
#                 return f'{version2} новее чем {version1}'
#         else:
#             # Если не удалось преобразовать в число, сравниваем строки
#             if c1 > c2:
#                 return f'{version1} новее чем {version2}'
#             elif c1 < c2:
#                 return f'{version2} новее чем {version1}'
#
#     # Если все компоненты одинаковы, сравниваем длину версий
#     if len(components1) > len(components2):
#         return f'{version1} новее чем {version2}'
#     elif len(components1) < len(components2):
#         return f'{version2} новее чем {version1}'
#     else:
#         return 'Версии идентичны'
#
# # Пример использования
# version = '12.23.1.33'
# rise_version = '12.23.1.333d'
#
# result = compare_versions(version, rise_version)
# print(result)


