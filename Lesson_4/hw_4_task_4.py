# Задача 4
#
# Напишіть за допомогою f-string та format. Дві стрічки де буде підставлятись імя та вік з зміних
#
# name = "оЛенА"
#
# age = 21
#
# f_string = тут ваш код формата ф-стрінг. | повино вийти -> Я Олена, мені 21 рік
#
# format_string = тут ваш код формата формат стрінг | повино вийти -> Я Олена, мені 21 рік
#
# print(f_string)
#
# print(format_string)


name = "оЛенА"
age = 21

f_string = f'Я {name.title()}, мені {age} рік'  #

format_string = """Я {name}, мені {age} рік""".format(name=name.title(), age=age)

print(f_string)

print(format_string)
