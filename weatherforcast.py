import requests
from datetime import datetime
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
            )
        data = r.json()
        pprint(data)
        
        city = data['name']
        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']

        print(f'{datetime.now()}\n'
        f'Погода в городе: {city}\nТемпература: {cur_weather} C°\n'
        f'Влажность: {humidity} %\nДавление: {pressure} мм р.т.\n'
        f'Скорость ветра: {wind_speed} м/с')



    except Exception as ex:
        print(ex)
        print('Проверьте название города')


def main():
    city = input('Введите город: ')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()

