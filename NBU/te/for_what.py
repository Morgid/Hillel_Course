import datetime
import requests


def currency_response():
    response = requests.request(method="GET", url="https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    currency = response.json()
    status_code = response.status_code
    return print(currency), print(status_code)


def write_log():
    currency_rates = currency_response()
    with open("currency_rates_data.txt", "w", encoding='utf-8') as file:
        file.write(f'Дата створення запиту {datetime.date.today()} \n')
        currency_rate = ''
        for element in currency_rates:
            currency_rate = f"{element['txt']} to UAH: {element['rate']} \n"
            file.write(currency_rate)
        return currency_rate




# def test_currency():
#     assert currency_response()
#     assert 'text' in currency_response()
#     assert 'rate' in currency_response()


# def currency_rates():
#     # currency_all = currency_response()
#     currency_rate = ''
#     for element in currency_response():
#         currency_name = element['txt']
#         rates = element['rate']
#         currency_rate = f"{element['txt']} to UAH: {element['rate']} \n"
#
#         print(currency_rate)
#     return currency_rate
# #
# #
# def write_log():
#     ololo = currency_rates()
#     with open("currency_rates_data.txt", "w", encoding='utf-8') as file:
#         currency_list = ""
#         for element in ololo:
#             currency_list = element
#         file.write(currency_list)
#
currency_response()