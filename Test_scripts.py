# Задача 2
#
# Переробіть задачу з попереднього уроку враховуючи ваші знання з цього уроку, використайте цикл for in або while.

print('Покупки')
shopping_list = input('Додайте список покупок через пробіл: ').split()

if len(shopping_list) < 5:
    print('Товарів менше п`яти.', end='\nЗамало товарів, введіть, будь ласка, більше товарів у список наступного разу.')


else:
    delete_counter = 0
    while len(shopping_list) > 0 and delete_counter < 5:
        delete_counter += 1
        print('Список продуктів:', shopping_list)
        print('Кількість товарів у кошику:', len(shopping_list))
        delete_item = int(input(f'Введіть номер товару який хочете видалити зі списку (від 1 до {len(shopping_list)}): '))
        delete = shopping_list.pop(delete_item - 1)
        print()


    if len(shopping_list) == 0:
        yes_no = (input('Кошик пустий, бажаєте додати ще товарів? (y/n): '))

        if yes_no.lower() == 'y':
            shopping_list = (input('Додайте список покупок через пробіл: ').split())
            print('У кошику: ', shopping_list)
            print('Дякуємо за користування програмою :)')

        elif yes_no.lower() == 'n':
            print('У кошику не залишилось товарів', end='\nДякуємо за користування програмою :)')

        else:
            print('Приймається відповідь y або n')
    else:
        print(f'В кошику ще залишилось товарів = {len(shopping_list)}')
        yes_no = (input('Бажаєте додати ще товарів? (y/n): '))

        if yes_no.lower() == 'y':
            shopping_list.append(input('Додайте список покупок через пробіл: ').split())
            print('Список продуктів:', shopping_list)
            print('Дякуємо за користування програмою :)')

        elif yes_no.lower() == 'n':
            print('У кошику: ', shopping_list)
            print('Дякуємо за користування програмою :)')

        else:
            print('Приймається відповідь y або n')
































# print('Задача 1')
# customer_bill = input("Введіть вартість покупок: ").split()
# customer_bill = [float(i) for i in customer_bill]
# print('Сума в чеку: ', sum(customer_bill))
# tax = round(sum(customer_bill) * (6.5 / 100), 2)
# print('Податок:', tax)
# bill_with_tax = round(sum(customer_bill) + (sum(customer_bill) * (6.5 / 100)), 2)
# print('До сплати: ', bill_with_tax)
#
# discount = input('У вас є купон на знижку? (y/n): ')
#
# if discount.lower() == 'y':
#     discount_sum_percent = input('Знижка на суму чи на відсоток? (sum/per): ')
#
#     if discount_sum_percent.lower() == 'sum':
#         discount_customer = float(input('Введіть суму знижки: '))
#
#         if discount_customer > bill_with_tax:
#             print('Ваша знижка перевищує суму чека.', end='\nСума до сплати не може бути від`ємною!')
#
#         else:
#             discount_sum = int(bill_with_tax) - int(discount_customer)
#             discount_sum_not_round = bill_with_tax - discount_customer
#             round_sum_bill = round((discount_sum_not_round - discount_sum), 2)
#
#             if round_sum_bill > 0.44:
#                 discount_sum = int(discount_sum) + 1
#                 print('Сума до сплати разом зі знижкою: ', discount_sum)
#
#             if round_sum_bill == 0.44:
#                 print('Сума до сплати разом зі знижкою: ', discount_sum_not_round)
#
#             if round_sum_bill < 0.44:
#                 discount_sum = int(discount_sum)
#                 print('Сума до сплати разом зі знижкою: ', discount_sum)
#
#     if discount_sum_percent.lower() == 'per':
#         percent = float(input('Веддіть відсоток знижки: '))
#         percent_customer = bill_with_tax * (percent / 100)
#         discount_customer_per = round((bill_with_tax - percent_customer), 2)
#
#         if discount_customer_per < 0:
#             print('Ваша знижка не може бути більше ніж 100%.', end='\nСума до сплати не може бути від`ємною!')
#
#         else:
#             round_per_bill = round(discount_customer_per - int(discount_customer_per), 2)
#
#             if round_per_bill > 0.44:
#                 discount_percent = int(discount_customer_per) + 1
#                 print('Сума до сплати разом зі знижкою: ', discount_percent)
#
#             if round_per_bill == 0.44:
#                 print('Сума до сплати разом зі знижкою: ', discount_customer_per)
#
#             if round_per_bill < 0.44:
#                 discount_percent = int(discount_customer_per)
#                 print('Сума до сплати разом зі знижкою: ', discount_percent)
#
# elif discount.lower() == 'n':
#     print('До сплати: ', bill_with_tax)
#
# else:
#     print('Вкажіть на наявність купону y або n.')
