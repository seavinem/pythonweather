import telebot
from datetime import *
bot = telebot.TeleBot('5413234713:AAHSIDP14ek-5W-DAVvXwUoA27YAr6sT4cc')

from pyowm import OWM
from pyowm.utils.config import get_default_config

language = get_default_config()
language['language'] = 'ru'
owm = OWM("5908d8edff957ce9f86b00f7f721b0ba", language)


now = datetime.now()

keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('привет', 'пока', 'дата')
keybord1.row('погода')


@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, 'привет, ты запустил меня', reply_markup = keybord1)

weat = 0

data = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
week = {1: 'понедельник', 2: 'вторник', 3: 'среда', 4: 'четверг', 5: 'пятница', 6: 'суббота', 7: 'воскресенье'}

@bot.message_handler(content_types=['text'])
def send_text(message):
    global weat
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'и тебе привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'до встречи!')
    elif any([message.text.lower() == 'дата', message.text.lower() == 'время', message.text.lower() == 'date', message.text.lower() == 'time']):
        bot.send_message(message.chat.id, f'сегодня {week[now.weekday()+1]} {now.day} {data[now.month]} {now.year} года')
        if now.minute >= 10:
            bot.send_message(message.chat.id, f'{now.hour}:{now.minute}')
        else:
            bot.send_message(message.chat.id, f'{now.hour}:0{now.minute}')
    elif message.text.lower() == 'погода':
        bot.send_message(message.chat.id, 'введите ваш город')
        weat = 1
    elif weat == 1:
        town = message.text.title()
        manager = owm.weather_manager()
        observation = manager.weather_at_place(town)
        weather = observation.weather
        stats = (f'сейчас на улице: {weather.detailed_status}\n'
                 f'облачность: {weather.clouds} %\n'
                 f'текущая температура: {weather.temperature("celsius").get("temp")} градусов\n'
                 f'максимальная температура: {weather.temperature("celsius").get("temp_max")} градусов\n'
                 f'минимальная температура: {weather.temperature("celsius").get("temp_min")} градусов\n'
                 f'сейчас ощущается: {weather.temperature("celsius").get("feels_like")} градусов\n'
                 f'скорость ветра: {weather.wind()["speed"]} м/с\n')
        if len(weather.rain) == 0:
            stats = stats + 'за последний час не было осадков'

        else:
            stats = stats + f"за последний час выпало осадков: {weather.rain['1h']} мм"
        bot.send_message(message.chat.id, f'{stats}')
        weat = 0



bot.polling()