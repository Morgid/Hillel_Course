# Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно).
# (так як робили на уроці). Ці значення запишіть в словник з відповідними ключами "+", "-", "/", "*"
#
# Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити
# (додавання, віднімання, множення, ділення). і виведіть йому цю табличку.


# Multiplication table
multi_list = []
for i in range(2, 10):
    for j in range(1, 10):
        multi_list.append(f"{i} * {j} = {i * j}")

# Addition table
addition_list = []
for i in range(2, 10):
    for j in range(1, 10):
        addition_list.append(f"{i} + {j} = {i + j}")

# Division table
division_list = []
for i in range(2, 10):
    for j in range(1, 10):
        division_list.append(f"{i} - {j} = {i - j}")

# Subtraction table
substract_list = []
for i in range(2, 10):
    for j in range(1, 10):
        substract_list.append(f"{i} / {j} = {round((i / j), 2)}")

table_dict = {"+": [addition_list], "-": [division_list], "/": [substract_list], "*": [multi_list]}

need_table = input("Яку табличку ви хочете побачити? (+, -, /, *): ")

if (need_table) == "+" or need_table.title() == "Додавання":
    print("Таблиця додавання: ")
    print(table_dict.get("+"))
elif need_table == "-" or need_table.title() == "Віднімання":
    print("Таблиця віднімання: ")
    print(table_dict.get("-"))
elif need_table == "/" or need_table.title() == "Ділення":
    print("Таблиця ділення: ")
    print(table_dict.get("/"))
elif need_table == "*" or need_table.title() == "Множення":
    print("Таблиця множення: ")
    print(table_dict.get("*"))
else:
    print("Будь ласка, виберіть таблицю ще раз")
