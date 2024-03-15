import random

def password_length():
    pass_len = int(input('Скільки символів має містити пароль?: '))
    return pass_len

def need_random_number():
    if input('Використовувати в паролі цифри?(Так/Ні): ').lower() == 'так':
        return True

def need_random_ukr_letter_little():
    if input('Використовувати в паролі маленькі укр. літери?(Так/Ні): ').lower() == 'так':
        return True

def need_random_ukr_letter_big():
    if input('Використовувати в паролі великі укр. літери?(Так/Ні): ').lower() == 'так':
        return True

def need_random_latin_letter_little():
    if input('Використовувати в паролі маленькі латинські літери?(Так/Ні): ').lower() == 'так':
        return True

def need_random_latin_letter_big():
    if input('Використовувати в паролі великі латинські літери?(Так/Ні): ').lower() == 'так':
        return True

def need_random_symbols():
    if input('Використовувати в паролі символи?(Так/Ні): ').lower() == 'так':
        return True

def random_number():
    list_numbers = '1234567890'
    return random.choice(list_numbers)

def random_ukr_letter_little():
    list_alphabet_ukr_little = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    return random.choice(list_alphabet_ukr_little)

def random_ukr_letter_big():
    list_alphabet_ukr_big = ['А', 'Б', 'В', 'Г', 'Ґ', 'Д', 'Е', 'Є', 'Ж', 'З', 'И', 'І', 'Ї', 'Й', 'К', 'Л', 'М', 'Н',
                             'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я']
    return random.choice(list_alphabet_ukr_big)


def random_latin_letter_little():
    list_alphabet_latin_little = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                                  's',
                                  't', 'v', 'x', 'y', 'z']
    return random.choice(list_alphabet_latin_little)


def random_latin_letter_big():
    list_alphabet_latin_big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
    return random.choice(list_alphabet_latin_big)


def random_symbols():
    list_symbols = ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', "\\", ']', '^', '_', '`', '{', '|', '}', '~'
    return random.choice(list_symbols)


def param_pass():
    pass_len = password_length()
    check_numb = need_random_number()
    check_ukr_little_letters = need_random_ukr_letter_little()
    check_ukr_big_letters = need_random_ukr_letter_big()
    check_latin_little_letters = need_random_latin_letter_little()
    check_latin_big_letters = need_random_latin_letter_big()
    check_symbols = need_random_symbols()

    password = ''
    for i in range(pass_len):
        if check_numb is True:
            password += random_number()
        if check_ukr_little_letters is True:
            password += random_ukr_letter_little()
        if check_ukr_big_letters is True:
            password += random_ukr_letter_big()
        if check_latin_little_letters is True:
            password += random_latin_letter_little()
        if check_latin_big_letters is True:
            password += random_latin_letter_big()
        if check_symbols is True:
            password += random_symbols()
        password = password[0:pass_len]
    return password

def shuffle_pass():
    p = param_pass()
    passw_gen = []
    for i in p:
        passw_gen.append(i)
    random.shuffle(passw_gen)
    client_pass = ''
    for i in passw_gen:
        client_pass += i
    return client_pass

print(shuffle_pass())


# def gener_pass():
#     check_pass = param_pass()
#     pass_len = password_length()




# f'Ваш пароль: {password}'


# print(int(random.random() * 10))
# print(f'{random.sample(list_alphabet_ukr_big, k=10)} {int(random.random() * 10)}')

# for i in list_alphabet_ukr_big:
#
#     for j in range(20):
#         print(i)
# print(f'{random.sample(list_alphabet_ukr_big, k=10)}')

# print(random.choice(list_alphabet_latin_big))

# def generate():
#     password = ''
#     for i in range(1):
#         password += f'{random.choice(random_symbols)}'.join(random_latin_letter_big)
#         # + random.choice(list_alphabet_ukr_little)+ random.choice(list_alphabet_ukr_big)+ random.choice(list_alphabet_latin_little)+ random.choice(list_alphabet_latin_big) + random.choice(list_symbols)}'
#     print(password)

# print(''.join(need_random_number()))
# # print('Ваш пароль:'.join(random_symbols().random_latin_letter_big()))

# for i in range(2):
#     print((need_random_number().join(need_random_number())))

# generate()
# print(random.choice(list_alphabet_latin_big))
