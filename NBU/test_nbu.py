import json
import datetime


def text_exchange():
    with open("exchange.json", "r", encoding='utf-8') as file:
        file_content = file.read()
        exchange = (json.loads(file_content))
        # with open('exchange_list.txt', 'w', encoding='utf-8') as file:
        #     file.write(f'???? ????????? ?????? {datetime.date.today()} \n')
        #     currency_rate = ''
        for element in exchange:
            currency_rate = f"{element['txt']} to UAH: {element['rate']} \n"
            # file.write(currency_rate)
        return currency_rate


def write_log(text_exchange):
    with open('exchange_list.txt', 'w', encoding='utf-8') as file:
        file.write(f'???? ????????? ?????? {datetime.date.today()} \n')
        currency_rate_write = text_exchange(currency_rate)
        for element in exchange:
            currency_rate = f"{element['txt']} to UAH: {element['rate']} \n"
            file.write(currency_rate)




# print(test_exchange())

# def write_currency_log(test_exchange):
#     # with open('exchange_list.txt', 'w', encoding='utf-8') as file:
#     #     for i in file.write(test_exchange):
#     with open('exchange_list.txt', 'w', encoding='utf-8') as file:
#         text = ""
#         for i in file.write(test_exchange):
#             text = i
#         file.write(text)
