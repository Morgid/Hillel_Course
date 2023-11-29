# Візьміть дві задачі з попередніх уроків, перша легка по вирішенню(декілька стрічок),
# друга більш складна і перепишіть їх на функції. Памятайте про Атамарність та god object.
# Там де написано що користувач має щось ввести то перероблюємо на функція приймає.
# Подивіться може можна за допомогою функції спростити код. В домашку вставте будь ласка опис задачі
# (далі(один з наступних уроків) буде домашка вашу домашку покрити тестами, але ми трохи поміняємо варіанти).


# Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно).
# (так як робили на уроці). Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
#
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.


def need_table():
    need_table = input("Яку табличку ви хочете побачити? (+, -, /, *): ")

    if need_table in table_dict:
        display_table(need_table)
    else:
        print("Будь ласка, виберіть таблицю ще раз")


def multiplication():
    multi_list = []
    for i in range(2, 10):
        for j in range(1, 10):
            multi_list.append(f"{i} * {j} = {i * j}")
    return multi_list


def subtraction():
    substract_list = []
    for i in range(2, 10):
        for j in range(1, 10):
            substract_list.append(f"{i} / {j} = {round((i / j), 2)}")
    return substract_list


def division():
    division_list = []
    for i in range(2, 10):
        for j in range(1, 10):
            division_list.append(f"{i} - {j} = {i - j}")
    return division_list


def addition():
    addition_list = []
    for i in range(2, 10):
        for j in range(1, 10):
            addition_list.append(f"{i} + {j} = {i + j}")
    return addition_list


table_dict = {
    "+": [addition()],
    "-": [division()],
    "/": [subtraction()],
    "*": [multiplication()]}


def display_table(need_table):
    if need_table == "+":
        print("Таблиця додавання:")
        print(table_dict.get("+"))

    elif need_table == "-":
        print("Таблиця віднімання:")
        print(table_dict.get("-"))

    elif need_table == "/":
        print("Таблиця ділення:")
        print(table_dict.get("/"))

    elif need_table == "*":
        print("Таблиця множення:")
        print(table_dict.get("*"))

    else:
        print("Будь ласка, виберіть таблицю ще раз")
        return


need_table()


# print(type(addition(addition_list)))