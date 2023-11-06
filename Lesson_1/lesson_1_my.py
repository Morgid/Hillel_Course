# коментар записується через решітку

# Якщо використовувати Alt, то через нього можна писати одразу в декількох стрічках
# Приклад:
#Сл'Вставлено через Alt'ово
#Сло'Вставлено через Alt'во
#Слов'Вставлено через Alt'о
#Слово

#В англ роскладці ctrl+? буде закоментовано все що виділено. Приклад:
# ввв
#
# ава
# ва
# ва
# ава
#Кінець прикладу.

# не пишіть змінні Україньскою мовою або латиницею Укр назви. Пишіть англійською код правильно.
# зміна = 20
# print(зміна)


variable_1 = 20
variable_2 = 5
variable_3 = 3

# hotkey дублювання ctrl+d


# print(variable_1 * variable_2) # без збереження в змінну
#
# result = variable_2 - variable_1 # більш правильний в написанні варіант
# print(result)

# # залишок від ділення % (будемо ділити до останнтого, 20-3=17, 17-3=16 і тд. і тп.
# result = variable_1 % variable_3 # 2
# print(result)

# # скільки разів ми змогли поділити на ціло // # 6
# result = variable_1 // variable_3
# print(result)

# Не можна починати змінну з цифри:
# 2_variavle = 10
# print(2_variavle)




#todo питання співбесіди: Які є типи данних в пайтоні str (стринг, все шо хош) та int (цифри)

# str
# sample_text = "Привіт, мене звуть Андрій"
# print(sample_text)
# print(type(sample_text))

# Конкатинація - додаються стрічки, зліплюються
# sample_text_1 = "999"
# sample_text_2 = "1"
# print(sample_text_1)
# print(type(sample_text_1))
# print(sample_text_1 + sample_text_2)
#
# sample_text_1_int = int(sample_text_1) # трансформування типу данних
# sample_text_2_int = int(sample_text_2) # трансформування типу данних
# result = (sample_text_1_int + sample_text_2_int)
# print(result)


age = int(input("Скільки вам років"))
print(age)
print(type(age))


