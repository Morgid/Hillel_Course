import datetime

import pytest
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


currency_response()

# @pytest.mark.parametrize(currency_response(), 'currency', ['txt', 'rate'])
def test_currency(status_code):
    check = currency_response()
    assert response.status_code
    assert 'text' in currency_response()
    # assert 'rate' in currency_response()