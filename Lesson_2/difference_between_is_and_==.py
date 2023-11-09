# чому різниця між is та ==

# "is" - це оператор з порівняння по id
#в той час як "==" - це поріняння по значенню
# Функція id() повертає унікальний ідентифікатор об’єкта, який призначається під час створення об’єкта.
# В PyCharm id деяких змінних
# # var_1 = 30
# # var_2 = 29+1
# будуть однакові, так як PyCharm намагається оптимізувати код і зберігає данні в одній області пам'яті.
# Якщо змінні потрапляют в один діапазон від -5 до 256 тоді id будуть однакові при використанні is та ==
# var_1 = 30
# var_2 = 29+1
# var_1 == var_2
# True
# var_1 is var_2
# True
# var_1 = 30
# id(var_1)
# 140711228198232
# var_2 = 29+1
# id(var_2)
# 140711228198232
# якщо змінні не потрапляют в один діапазон від -5 до 256 тоді id будуть відрізнятися, тобто записуватись в різні області пам'яті,
# але при цьому == буде True
# var_1 = 1000
# var_2 = 999+1
# var_1 is var_2
# False
# var_1 == var_2
# True
#var_1 = 1000
# id(var_1)
# 2528495045680
# var_2 = 999+1
# id(var_2)
# 2528495056784
# Для наглядності використовувалась консоль Python.




