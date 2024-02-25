import datetime
import requests


def currency_response():
    response = requests.request(method="GET", url="https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
    if response.status_code == 200:
        currency = response.json()
        return currency, 200
    else:
        print(f"Помилка {response.status_code}")


def write_currency_rates():
    currency_rates, status_code = currency_response()
    with open("currency_rates_data.txt", "w", encoding='utf-8') as file:
        file.write(f'Дата створення запиту {datetime.date.today()} \n')
        currency_rate = ''
        for element in currency_rates:
            currency_rate = f"{element['txt']} to UAH: {element['rate']} \n"
            file.write(currency_rate)
        return currency_rate


write_currency_rates()
