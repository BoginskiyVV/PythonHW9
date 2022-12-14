import requests
from datetime import datetime
from config import open_weather_token, telegram_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=telegram_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def start_command(message: types.Message):
    await message.reply(f'/weather_forcast\n/currency_rate')


@dp.message_handler(commands=['currency_rate'])
async def currency_rate_command(message: types.Message):
    cur = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    list_cur = cur.json()
    eur = list_cur['Valute']['EUR']['Name']
    eur_value = list_cur['Valute']['EUR']['Value']
    gbp = list_cur['Valute']['GBP']['Name']
    gbp_value = list_cur['Valute']['GBP']['Value']
    usd = list_cur['Valute']['USD']['Name']
    usd_value = list_cur['Valute']['USD']['Value']
    await message.reply(f'Курс ЦБ РФ на {datetime.now()}\n'
                        f'1 {usd} - {usd_value} российских рублей\n'
                        f'1 {gbp} - {gbp_value} российских рублей\n'
                        f'1 {eur} - {eur_value} российских рублей\n')

    # await message.reply('Введите буквенный код валюты EUR, GBP или USD: ')
    # cur = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    # if message.reply == 'EUR':
    #     list_cur = cur.json()
    #     cur = list_cur['Valute']['EUR']['Name']
    #     value = list_cur['Valute']['EUR']['Value']
    #     print(f'Курс ЦБ РФ на {datetime.now()}\n'
    #           f'1 {cur} - {value} российских рублей')
    # elif message.reply == 'GBP':
    #     list_cur = cur.json()
    #     cur = list_cur['Valute']['GBP']['Name']
    #     value = list_cur['Valute']['GBP']['Value']
    #     print(f'Курс ЦБ РФ на {datetime.now()}\n'
    #           f'1 {cur} - {value} российских рублей')
    # elif message.reply == 'USD':
    #     list_cur = cur.json()
    #     cur = list_cur['Valute']['USD']['Name']
    #     value = list_cur['Valute']['USD']['Value']
    #     print(f'Курс ЦБ РФ на {datetime.now()}\n'
    #           f'1 {cur} - {value} российских рублей')
    # print('Утоните курс какой валюты вас интересует')
    # await message.reply(f'Утоните курс какой валюты вас интересует')


@dp.message_handler(commands=['weather_forcast'])
async def weather_forcast_command(message: types.Message):
    await message.reply('Напиши латиницей город, чтобы узнать погоду')


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
            )
        data = r.json()
        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']

        await message.reply(f'{datetime.now()}\n'
                            f'Погода в городе: {city}\nТемпература: {cur_weather} C°\n'
                            f'Влажность: {humidity} %\nДавление: {pressure} мм р.т.\n'
                            f'Скорость ветра: {wind_speed} м/с')

    except:
        await message.reply('Проверьте название города')


if __name__ == '__main__':
    print('Server start')
    executor.start_polling(dp)