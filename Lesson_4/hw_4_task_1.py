
# Задача 1
# Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл,
# точна кількість не вказана. Вам потрібно до вартості покупок додати 6,5 відсотки податків.
# Потім питаєте чи є в користувача купон на знижку якщо є то питаєте це на суму чи на відсоток
# і потім віднімаєте суму або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.
# * завдання з зірочкою не впливає на бал.
# Округліть суму якщо копійок більше ніж 44 то це буде + 1 гривня, якщо менше.
# то тоді просто відкидаємо копійки від ціни.
#
#    213 123 213 2.2 2.2 2.3

import math
import decimal
print('Задача 1')
customer_bill = input("Введіть вартість покупок: ").split()
customer_bill = [float(i) for i in customer_bill]
print('Сума в чеку: ', sum(customer_bill), 'грн.')
tax = round(sum(customer_bill) * (6.5 / 100), 2)
print(f'Податок: {tax} грн.')
bill_with_tax = round(sum(customer_bill) + (sum(customer_bill) * (6.5 / 100)), 2)

# round_sum_bill = bill_with_tax - int(bill_with_tax)
# if round_sum_bill > 0.44:
#     bill_with_tax = int(bill_with_tax) + 1
#     print('До сплати: ', bill_with_tax, 'грн.')
#
# else:
#     bill_with_tax = int(bill_with_tax)
#     print('До сплати: ', bill_with_tax)
print('До сплати: ', bill_with_tax)

discount = input('У вас є купон на знижку? (y/n): ')

if discount.lower() == 'y':
    discount_sum_percent = input('Знижка на суму чи на відсоток? (sum/per): ')

    if discount_sum_percent.lower() == 'sum':
        discount_customer = float(input('Введіть суму знижки: '))

        if discount_customer > bill_with_tax:
            print('Сума до сплати не може бути від`ємною!')
        else:
            discount_sum = (bill_with_tax - discount_customer)
            discount_sum_not_round = (bill_with_tax - discount_customer)

            round_sum_bill = discount_sum - int(discount_sum)
            if round_sum_bill > 0.44:
                discount_sum = int(discount_sum) + 1
                print('Сума до сплати разом зі знижкою: ', discount_sum)

            elif round_sum_bill == 0.44:
                print('Сума до сплати разом зі знижкою: ', discount_sum_not_round)

            else:
                discount_sum = int(discount_sum)
                print('Сума до сплати разом зі знижкою: ', discount_sum)

            print('Сума до сплати разом зі знижкою: ', discount_sum)
    elif discount_sum_percent.lower() == 'per':
        percent = float(input('Веддіть відсоток знижки: '))
        discount_percent = round(bill_with_tax - (bill_with_tax * (percent / 100)), 2)

        if discount_percent < 0:
            print('Сума до сплати не може бути від`ємною!')

        else:
            print('Сума до сплати разом зі знижкою: ', discount_percent)
    else:
        print('Якщо у вас є знижка вкажіть sum або per')
else:
    print('До сплати: ', bill_with_tax)

