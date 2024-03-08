import random


list_numbers = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'

list_alphabet_ukr_little = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н',
                            'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']

list_alphabet_ukr_big = ['А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н',
                         'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я']

list_alphabet_latin_little = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                              't', 'v', 'x', 'y', 'z']

list_alphabet_latin_big = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z'

list_symbols = ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>','?','@', '[', "\\", ']', '^', '_', '`', '{', '|', '}', '~'

# print(int(random.random() * 10))
# print(f'{random.sample(list_alphabet_ukr_big, k=10)} {int(random.random() * 10)}')

# for i in list_alphabet_ukr_big:
#
#     for j in range(20):
#         print(i)
# print(f'{random.sample(list_alphabet_ukr_big, k=10)}')

# print(random.choice(list_alphabet_latin_big))

def generate(list_numbers: None, list_alphabet_ukr_little: None):
    password = ''
    for i in range(1):
        password += f'{random.choice(list_numbers)}'
        # + random.choice(list_alphabet_ukr_little)+ random.choice(list_alphabet_ukr_big)+ random.choice(list_alphabet_latin_little)+ random.choice(list_alphabet_latin_big) + random.choice(list_symbols)}'
    print(password)


if __name__ == "__main__":

generate(list_numbers)
# print(random.choice(list_alphabet_latin_big))