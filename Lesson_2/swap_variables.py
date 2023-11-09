print('Поміняйте місцями 2 змінні не використовуючи третю змінну')
print()

print('Початкові умови')
variable_1 = 10
variable_2 = 20
print('Перша змінна:',variable_1)
print('Друга змінна:',variable_2)
print()

print('1. Синтаксичний цукор')
variable_1, variable_2 = variable_2, variable_1
print(variable_1)
print(variable_2)
print()

print('2. Довавання та віднімання')
variable_1 = 10
variable_2 = 20
variable_2 = variable_1 + variable_2
print(variable_2)
variable_1 = variable_2 - variable_1
print(variable_1)
variable_2 = variable_2 - variable_1
print(variable_2)
print()

print('3. Множення та ділення')
variable_1 = 10
variable_2 = 20
variable_2 = variable_2 / variable_1
print(variable_2)
variable_1 = variable_1 * variable_2
print(int(variable_1))
variable_2 = variable_1 / variable_2
print(int(variable_2))

