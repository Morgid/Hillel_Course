import json
import datetime


def text_exchange():
    with open("exchange.json", "r", encoding='utf-8') as file:
        file_content = file.read()
        exchange = (json.loads(file_content))
        for element in exchange:
            currency_rate = f"{element['txt']} to UAH: {element['rate']} \n"
            # print(currency_rate)
        return currency_rate


def write_log(text_exchange):
    text_exchange
    currency_rate_write = ''
    with open('exchange_list.txt', 'w', encoding='utf-8') as file:
        file.write(f'Дата створення запиту {datetime.date.today()} \n')
        for element in text_exchange():
            currency_rate_write = f"{element['txt']} to UAH: {element['rate']} \n"
            file.write(currency_rate_write)
        return currency_rate_write

text_exchange()
write_log()
