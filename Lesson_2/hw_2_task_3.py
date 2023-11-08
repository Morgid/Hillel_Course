# Задача 3

# Напишіть програму яка в користувача запитує два числа(можуть бути числа типу інт, а можуть бути в стр).
# Потім запитує це стр чи інт і в залежності від відповіді конкатенує їх або додає і повертає результат перемножений
# на три.
# якщо після конкатенації отримали 10 то перемноживши на 3 отримаємо 30.

# Рішення задачі.
print('Задача 3')
number_1 = input('Введіть перше число: ')
number_2 = input('Введіть друге число: ')
numbers_type = input('Вкажіть який тип чисeл, int або str: ')
if numbers_type.lower() == 'str':
    concatenation = (number_1 + number_2)
    print('Конкатенація =', concatenation)
    if concatenation == '10':
        concatenation = int(concatenation) * 3
        print('Якщо після конкатенації отримали 10 то множимо на 3 =', concatenation)
elif numbers_type == 'int':
        sum_numbers = (int(number_1) + int(number_2))*3
        print('Результат додавання та перемноження на 3 =', sum_numbers)
else:
        print('Невірні типи даних')






# Чорновий варіант, не впевнений чи правильно я зрозумів умови задачі спочатку :)

# print('Задача 3')
# number_1 = input('Введіть перше число: ')
# number_2 = input('Введіть друге число: ')
# number_type_1 = input('Вкажіть який тип першого числа, int або str: ')
# number_type_2 = input('Вкажіть який тип другого числа, int або str: ')
# if number_type_1.lower() + number_type_2.lower() == 'strstr':
#     concatenation = (number_1 + number_2)
#     print('Конкатенація =', concatenation)
#     if concatenation == '10':
#         concatenation = int(concatenation) * 3
#         print('Якщо після конкатенації отримали 10 то множимо на 3 =', concatenation)
# else:
#     if number_type_1.lower() + number_type_2.lower() == 'intint':
#         sum_numbers = (int(number_1) + int(number_2))*3
#         print('Результат додавання та перемноження на 3 =', sum_numbers)
#     else:
#         print('Невірні типи даних')