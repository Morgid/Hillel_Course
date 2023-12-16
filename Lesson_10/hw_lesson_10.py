# Задача 2
# Візьміть задачу з минулого уроку(
# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її всіма трьома методами
# ) модернізуйте її так що кожний раз коли ми її запускаємо те що ми туди передаєм та результат повинно записуватись в файл log.txt
# Зверніть увагу на те що в файл повинно дозаписуватись, а не затератись.
# Уявіть що ця функція являється легасі кодом і ви її не можете змінювати,
# тому потрібно використовувати декоратор. Я хотів би бачити таку реалізацію в домашці три функції:
# функція з минулого уроку
# функція що записую текст
# і декоратор

def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result


def write_log(func):
    def wrapper(*args):
        with open('log.txt', 'a') as file:
            file.write('\n')
            file.write('---------START---------\n')
            file.write(f'Adding numbers {args[0]}, {args[1]}, {args[2]}\n')
            file.write(f'Result = {add_three_numbers(*args)}\n')
            file.write('----------END----------\n')
        result = func(*args)
        return result

    return wrapper


@write_log
def foo(*args):
    print(f'The result of adding {args[0]}, {args[1]}, {args[2]} in log.txt')


foo(8, 32, 110)


# Рекурсія
# Не оцінюється
# Напишіть рекурсивну функцію яка приймає число і повертає добуток всіх чисел якщо віднімати мінус
# 1. тобто якщо передати в функцію 4 то в нас буде 4+3+2+1 = 10.
def recursion(i: int) -> int:
    if i <= 1:
        return 1
    return i + recursion(i - 1)


print(recursion(11))
