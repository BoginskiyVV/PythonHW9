import requests
import json
from pprint import pprint
from datetime import datetime


def get_currency():
    user_request = input('Введите буквенный код валюты EUR, GBP или USD: ').upper()
    cur = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    if user_request == 'EUR':
        list_cur = cur.json()
        cur = list_cur['Valute']['EUR']['Name']
        value = list_cur['Valute']['EUR']['Value']
        print(f'Курс ЦБ РФ на {datetime.now()}\n'
              f'1 {cur} - {value} российских рублей')
    elif user_request == 'GBP':
        list_cur = cur.json()
        cur = list_cur['Valute']['GBP']['Name']
        value = list_cur['Valute']['GBP']['Value']
        print(f'Курс ЦБ РФ на {datetime.now()}\n'
              f'1 {cur} - {value} российских рублей')
    elif user_request == 'USD':
        list_cur = cur.json()
        cur = list_cur['Valute']['USD']['Name']
        value = list_cur['Valute']['USD']['Value']
        print(f'Курс ЦБ РФ на {datetime.now()}\n'
              f'1 {cur} - {value} российских рублей')
    else:
        print('Утоните курс какой валюты вас интересует')


get_currency()
