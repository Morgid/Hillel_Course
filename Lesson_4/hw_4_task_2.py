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
        delete_item = int(                          # так мені родзілило стрічку комбінація ctrl + alt + l
            input(f'Введіть номер товару який хочете видалити зі списку (від 1 до {len(shopping_list)}): '))
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
