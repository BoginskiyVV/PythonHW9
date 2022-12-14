from telegram import Update
from pprint import pprint
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from datetime import datetime
import requests
from cfg import tlg
from weatherforcast import main, get_weather


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # log(update, context)
    await update.message.reply_text(f'/hello\n/time\n/help\n/weather_forcast\n/currency_rate')


async def get_w(update: Update, context: ContextTypes.DEFAULT_TYPE):
    get_weather()


    # await update.message.reply_text(f'Введите город латиницей: ')


    # await update.message.reply_text(f'Введите город латиницей: ')


    # print(msg)


    # r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={c}&appid={wtr}&units=metric')
    # data = r.json()
    # pprint(data)

    #
    # # # try:
    # # # await update.message.reply_text(f'Введите город: ')
    # #
    # # # msg = await update.message.reply_text(f'Введите город: ')
    # # c = await update.message.reply_text(f'Введите город: ')
    # r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={c}&appid={wtr}&units=metric')
    # data = r.json()
    # pprint(data)
    #
    # city = data['name']
    # cur_weather = data['main']['temp']
    # humidity = data['main']['humidity']
    # pressure = data['main']['pressure']
    # wind_speed = data['wind']['speed']
    #
    # await update.message.reply_text(f'{datetime.now()}\n'
    #                                 f'Погода в городе: {city}\nТемпература: {cur_weather} C°\n'
    #                                 f'Влажность: {humidity} %\nДавление: {pressure} мм р.т.\n'
    #                                 f'Скорость ветра: {wind_speed} м/с')
    # except:
    # await update.message.reply_text('Проверьте название города')
    # # log(update, context)
    # msg = update.message.text
    # print(msg)
    # items = msg.split()
    # x = int(items[1])
    # y = int(items[2])
    # await update.message.reply_text(f'{x} + {y} = {x+y}')


app = ApplicationBuilder().token(tlg).build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("weather_forcast", get_weather))


print('Server start')
app.run_polling()

#
# import requests
# import datetime
# from config import open_weather_token, telegram_token
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
#
# bot = Bot(token=telegram_token)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.reply('Напиши латиницей город, чтобы узнать погоду')
#
#
# @dp.message_handler()
# async def get_weather(message: types.Message):
#     try:
#         r = requests.get(
#             f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
#             )
#         data = r.json()
#         city = data['name']
#         cur_weather = data['main']['temp']
#         humidity = data['main']['humidity']
#         pressure = data['main']['pressure']
#         wind_speed = data['wind']['speed']
#
#         await message.reply(f'{datetime.datetime.now()}\n'
#             f'Погода в городе: {city}\nТемпература: {cur_weather} C°\n'
#             f'Влажность: {humidity} %\nДавление: {pressure} мм р.т.\n'
#             f'Скорость ветра: {wind_speed} м/с')
#
#     except:
#         await message.reply('Проверьте название города')
#
#
# if __name__ == '__main__':
#     print('Server start')
#     executor.start_polling(dp)


