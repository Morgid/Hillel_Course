# # # # Multiplication table
# # # multi_list = []
# # # for i in range(2, 10):
# # #     for j in range(1, 10):
# # #         multi_list.append(f"{i} * {j} = {i * j}")
# # #
# # # # Addition table
# # # addition_list = []
# # # for i in range(2, 10):
# # #     for j in range(1, 10):
# # #         addition_list.append(f"{i} + {j} = {i + j}")
# # #
# # # # Division table
# # # division_list = []
# # # for i in range(2, 10):
# # #     for j in range(1, 10):
# # #         division_list.append(f"{i} - {j} = {i - j}")
# # #
# # # # Subtraction table
# # # substract_list = []
# # # for i in range(2, 10):
# # #     for j in range(1, 10):
# # #         substract_list.append(f"{i} / {j} = {round((i / j), 2)}")
# # #
# # # table_dict = {"+": [addition_list], "-": [division_list], "/": [substract_list], "*": [multi_list]}
# # #
# # # need_table = input("Яку табличку ви хочете побачити? (+, -, /, *): ")
# # #
# # # if (need_table) == "+" or need_table.title() == "Додавання":
# # #     print("Таблиця додавання: ")
# # #     print(table_dict.get("+"))
# # # elif need_table == "-" or need_table.title() == "Віднімання":
# # #     print("Таблиця віднімання: ")
# # #     print(table_dict.get("-"))
# # # elif need_table == "/" or need_table.title() == "Ділення":
# # #     print("Таблиця ділення: ")
# # #     print(table_dict.get("/"))
# # # elif need_table == "*" or need_table.title() == "Множення":
# # #     print("Таблиця множення: ")
# # #     print(table_dict.get("*"))
# # # else:
# # #     print("Будь ласка, виберіть таблицю ще раз")
# # #
# # # def table_choice(subtraction_table, division_table):
# # #     need_table = input("Яку табличку ви хочете побачити? (+, -, /, *): ")
# # #
# # #
# # #
# # #
# # #
# # # if need_table == "+" or need_table.title() == "Додавання":
# # #     print("Таблиця додавання: ")
# # #     print(table_dict.get("+"))
# # # elif need_table == "-" or need_table.title() == "Віднімання":
# # #     print("Таблиця віднімання: ")
# # #     print(table_dict.get("-"))
# # # elif need_table == "/" or need_table.title() == "Ділення":
# # #     print("Таблиця ділення: ")
# # #     print(table_dict.get("/"))
# # # elif need_table == "*" or need_table.title() == "Множення":
# # #     print("Таблиця множення: ")
# # #     print(table_dict.get("*"))
# # # else:
# # #     print("Будь ласка, виберіть таблицю ще раз")
# # #
# # #     dict_1 = {'+': {}, '-': {}, '/': {}, '*': {}, }
# # #
# # #     oper = input("Виберіть операцію (+, -, *, /): ")
# # #
# # #
# # #     def filling_dict(oper):
# # #         for i in range(2, 10):
# # #             for j in range(2, 10):
# # #                 vol = eval(f"{i}{oper}{j}")
# # #                 dict_1[oper][i, j] = round(vol, 2)
# # #         return dict_1
# # #
# # #
# # #     def table(dict_1):
# # #         if oper in dict_1:
# # #             for i in range(2, 10):
# # #                 print()
# # #                 print(end=" ")
# # #                 for j in range(2, 10):
# # #                     print(f"{i} {oper} {j} = {dict_1[oper][i, j]}\n", end=" ")
# # #
# # #
# # #     filling_dict(oper)
# # #     table(dict_1)
# # #
# # # customer_bill = input("Введіть вартість покупок: ").split()
# # # customer_bill = [float(i) for i in customer_bill]
# # # def tax_function(customer_bill: float):
# # #     tax = round(sum(customer_bill) * (6.5 / 100), 2)
# # #     return tax
# # # print(tax_function(tax), tupe(tax_function(tax)))
# #
# #
# #
# print('Задача 1')
# customer_bill = input("Введіть вартість покупок: ").split()
#
# price_list = [float(i) for i in customer_bill]
# customer_bill = sum(price_list)
# print(f'Сума в чеку: {customer_bill} грн.')
#
#
# def tax_func(customer_bill: float):
#     tax = round(customer_bill * (6.5 / 100), 2)
#     return tax
#
#
# print(f'Податок: {tax_func(customer_bill)} грн.')
#
#
# def bill_with_tax_func(customer_bill: float):
#     bill_with_tax = round(customer_bill + ((customer_bill) * (6.5 / 100)), 2)
#     return bill_with_tax
#
# def checking_threshold_values(discount_customer: float | int):
#     discount_sum = int(bill_with_tax_func(customer_bill)) - int(discount_customer)
#     discount_sum_not_round = bill_with_tax_func(customer_bill) - discount_customer
#     round_sum_bill = round((discount_sum_not_round - discount_sum), 2)
#     return discount_sum, discount_sum_not_round, round_sum_bill
#
#
# print(f'До сплати: {bill_with_tax_func(customer_bill)} грн.')
#
# discount = input('У вас є купон на знижку? (y/n): ')
#
# if discount.lower() == 'y':
#     discount_sum_percent = input('Знижка на суму чи на відсоток? (sum/per): ')
#
#     if discount_sum_percent.lower() == 'sum':
#         discount_customer = float(input('Введіть суму знижки: '))
#
#         if discount_customer > bill_with_tax_func(customer_bill):
#             print('Ваша знижка перевищує суму чека.', end='\nСума до сплати не може бути від`ємною!')
#
#         elif checking_threshold_values(discount_customer) > 0.44:
#             discount_sum = int(checking_threshold_values(discount_customer)) + 1
#             print('Сума до сплати разом зі знижкою: ', discount_sum)
#
#         elif checking_threshold_values(discount_customer) == 0.44:
#             print('Сума до сплати разом зі знижкою: ', checking_threshold_values(discount_sum_not_round))
#
#         elif checking_threshold_values(discount_customer) < 0.44:
#             discount_sum = int(checking_threshold_values(discount_customer))
#             print('Сума до сплати разом зі знижкою: ', discount_sum)
#
#
#         # else:
#         #     discount_sum = int(bill_with_tax_func(customer_bill)) - int(discount_customer)
#         #     discount_sum_not_round = bill_with_tax_func(customer_bill) - discount_customer
#         #     round_sum_bill = round((discount_sum_not_round - discount_sum), 2)
#         #
#         #     if round_sum_bill > 0.44:
#         #         discount_sum = int(discount_sum) + 1
#         #         print('Сума до сплати разом зі знижкою: ', discount_sum)
#         #
#         #     if round_sum_bill == 0.44:
#         #         print('Сума до сплати разом зі знижкою: ', discount_sum_not_round)
#         #
#         #     if round_sum_bill < 0.44:
#         #         discount_sum = int(discount_sum)
#         #         print('Сума до сплати разом зі знижкою: ', discount_sum)
#
#     if discount_sum_percent.lower() == 'per':
#
#         def cheking_customer_persent(percent):
#             percent_customer = bill_with_tax_func(customer_bill) * (percent / 100)
#             discount_customer_per = round((bill_with_tax_func(customer_bill) - percent_customer), 2)
#             return discount_customer_per
#
#         percent = float(input('Веддіть відсоток знижки: '))
#         # percent_customer = bill_with_tax_func(customer_bill) * (percent / 100)
#         # discount_customer_per = round((bill_with_tax_func(customer_bill) - percent_customer), 2)
#
#         if cheking_customer_persent(percent) < 0:
#             print('Ваша знижка не може бути більше ніж 100%.', end='\nСума до сплати не може бути від`ємною!')
#
#         else:
#             round_per_bill = round(cheking_customer_persent(percent) - int(cheking_customer_persent(percent)), 2)
#
#             if round_per_bill > 0.44:
#                 discount_percent = cheking_customer_persent(percent) + 1
#                 print('Сума до сплати разом зі знижкою: ', discount_percent)
#
#             if round_per_bill == 0.44:
#                 print('Сума до сплати разом зі знижкою: ', cheking_customer_persent(percent))
#
#             if round_per_bill < 0.44:
#                 discount_percent = int(cheking_customer_persent(percent))
#                 print('Сума до сплати разом зі знижкою: ', discount_percent)
#
# elif discount.lower() == 'n':
#     print(f'До сплати: {bill_with_tax_func(customer_bill)} грн.')
#
# else:
#     print('Вкажіть на наявність купону y або n.')
#
#


def generate_table(operator):
    table_list = []
    for i in range(2, 10):
        for j in range(1, 10):
            if operator == "+":
                table_list.append(f"{i} + {j} = {i + j}")
            elif operator == "-":
                table_list.append(f"{i} - {j} = {i - j}")
            elif operator == "/":
                table_list.append(f"{i} / {j} = {round((i / j), 2)}")
            elif operator == "*":
                table_list.append(f"{i} * {j} = {i * j}")
    return table_list

def display_table(operator):
    if operator == "+":
        print("Таблиця додавання:")
    elif operator == "-":
        print("Таблиця віднімання:")
    elif operator == "/":
        print("Таблиця ділення:")
    elif operator == "*":
        print("Таблиця множення:")
    else:
        print("Будь ласка, виберіть таблицю ще раз")
        return

    table_data = table_dict.get(operator)
    if table_data:
        for entry in table_data[0]:
            print(entry)
    else:
        print("Таблиця порожня.")

def main():
    operator_input = input("Яку табличку ви хочете побачити? (+, -, /, *): ").lower()

    if operator_input in table_dict:
        display_table(operator_input)
    else:
        print("Будь ласка, виберіть таблицю ще раз")

if __name__ == "__main__":
    table_dict = {
        "+": [generate_table("+")],
        "-": [generate_table("-")],
        "/": [generate_table("/")],
        "*": [generate_table("*")]
    }

    main()
