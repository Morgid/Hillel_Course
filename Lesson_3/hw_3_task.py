# Задача 1
# Уявимо що до нас прийшов наш друг або подруга і попросили написати додаток для покупок в магазині
# що б можна було скласти список продуктів та коли купуєш викреслювати(для викреслення питайте номер елемента,
# що б видалити по індексу треба його передати в pop list_a.pop(0) - видалить нульовий індекс, памятайте що користувач не знає що в нас індекси починаються з нуля)
# Також нам відомо що цей список має пять або більше елементів.
# Після кожного видалення елементу виводьте наш оновлений список.
# Після 5 видалень перевірте чи список пустий якщо не пустий напишіть що ось ще є продукти, якщо пусти то напишіть про це.
# Також після цього кроку запропонуйте користувачу написати ще продуктів та додати його в кошик. і виведіть їх на екран. Але цього разу вже без видалень.
# кроки:
# Спочатку пропонуємо користувачу ввести продукти.
# Робимо 5 запитів на видалення
# Перевіряємо корзину
# Пропонуємо додати продукти
# Виводмо список і прощаємось


print('Покупки')
shopping_list = input('Додайте список покупок через пробіл: ').split()

if len(shopping_list) < 5:
    print('Товарів менше п`яти.',end='\nЗамало товарів, введіть, будь ласка, більше товарів у список наступного разу.')

else:
    print('Список продуктів:',shopping_list)
    print('Кількість товарів у кошику:', len(shopping_list))
    delete_item = int(input(f'Введіть номер товару який хочете видалити зі списку (від 1 до {len(shopping_list)}): '))
    delete = shopping_list.pop(delete_item - 1)
    print()

    print('Список продуктів:',shopping_list)
    print('Кількість товарів у кошику:', len(shopping_list))
    delete_item = int(input(f'Введіть номер товару який хочете видалити зі списку (від 1 до {len(shopping_list)}): '))
    delete = shopping_list.pop(delete_item - 1)
    print()

    print('Список продуктів:', shopping_list)
    print('Кількість товарів у кошику:', len(shopping_list))
    delete_item = int(input(f'Введіть номер товару який хочете видалити зі списку (від 1 до {len(shopping_list)}): '))
    delete = shopping_list.pop(delete_item - 1)
    print()

    print('Список продуктів:', shopping_list)
    print('Кількість товарів у кошику:', len(shopping_list))
    delete_item = int(input(f'Введіть номер товару який хочете видалити зі списку (від 1 до {len(shopping_list)}): '))
    delete = shopping_list.pop(delete_item - 1)
    print()

    print('Список продуктів:', shopping_list)
    print('Кількість товарів у кошику:', len(shopping_list))
    delete_item = int(input(f'Введіть номер товару який хочете видалити зі списку (від 1 до {len(shopping_list)}): '))
    delete = shopping_list.pop(delete_item - 1)
    print()

    print('Список продуктів:', shopping_list)
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
            update_shopping_list = shopping_list
            update_shopping_list.append(input('Додайте список покупок через пробіл: ').split())
            print('Список продуктів:', shopping_list)
            print('Дякуємо за користування програмою :)')

        elif yes_no.lower() == 'n':
            print('У кошику: ', shopping_list)
            print('Дякуємо за користування програмою :)')

        else:
            print('Приймається відповідь y або n')
