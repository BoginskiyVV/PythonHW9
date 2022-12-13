import requests
import datetime
from config import open_weather_token, telegram_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token = telegram_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
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
    executor.start_polling(dp)