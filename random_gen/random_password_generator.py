import random


def password_length():
    pass_len = input('Скільки символів має містити пароль?: ')
    if pass_len.isdigit():
        return int(pass_len)
    else:
        print('Ви ввели невірне значення, спробуйте ще раз.')
        quit()


def need_random_number():
    if input('Якщо бажаєте щоб в паролі були цифри, введіть "Так": ').lower() == 'так':
        return True


def need_random_ukr_letter_little():
    if input('Якщо бажаєте щоб в паролі були маленькі укр. літери, введіть "Так": ').lower() == 'так':
        return True


def need_random_ukr_letter_big():
    if input('Якщо бажаєте щоб в паролі були великі укр. літери, введіть "Так": ').lower() == 'так':
        return True


def need_random_latin_letter_little():
    if input('Якщо бажаєте щоб в паролі були маленькі латинські літери, введіть "Так": ').lower() == 'так':
        return True


def need_random_latin_letter_big():
    if input('Якщо бажаєте щоб в паролі були великі латинські літери, введіть "Так": ').lower() == 'так':
        return True


def need_random_symbols():
    if input('Якщо бажаєте щоб в паролі були символи, введіть "Так": ').lower() == 'так':
        return True


def random_number():
    list_numbers = '1234567890'
    return random.choice(list_numbers)


def random_ukr_letter_little():
    list_alphabet_ukr_little = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    return random.choice(list_alphabet_ukr_little)


def random_ukr_letter_big():
    list_alphabet_ukr_big = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    return random.choice(list_alphabet_ukr_big)


def random_latin_letter_little():
    list_alphabet_latin_little = 'abcdefghiklmnopqrstvxyz'
    return random.choice(list_alphabet_latin_little)


def random_latin_letter_big():
    list_alphabet_latin_big = 'ABCDEFGHIKLMNOPQRSTVXYZ'
    return random.choice(list_alphabet_latin_big)


def random_symbols():
    list_symbols = ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', "\\", ']', '^', '_', '`', '{', '|', '}', '~'
    return random.choice(list_symbols)


def param_pass():
    pass_len = password_length()
    if pass_len <= 0:
        print(f'Неможливо згенерувати пароль з {pass_len} символів!')
        quit()
    else:
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


def generate_password():
    passw_gen = []
    for i in param_pass():
        passw_gen.append(i)
    random.shuffle(passw_gen)
    gen_pass_result = ''
    for i in passw_gen:
        gen_pass_result += i
    if gen_pass_result == '':
        print('Пароль не може бути пустим, виберіть з яких символів пароль має бути сгенерований!')
        quit()
    else:
        return f'Ваш пароль: {gen_pass_result}'


print(generate_password())
