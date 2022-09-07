import telebot
from datetime import *
bot = telebot.TeleBot('5413234713:AAHSIDP14ek-5W-DAVvXwUoA27YAr6sT4cc')

now = datetime.now()

keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('привет', 'пока', 'дата')

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, 'привет, ты запустил меня', reply_markup = keybord1)

data = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
week = {1: 'понедельник', 2: 'вторник', 3: 'среда', 4: 'четверг', 5: 'пятница', 6: 'суббота', 7: 'воскресенье'}

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'и тебе привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'до встречи!')
    elif any([message.text.lower() == 'дата', message.text.lower() == 'время', message.text.lower() == 'date', message.text.lower() == 'time']):
        bot.send_message(message.chat.id, f'сегодня {week[now.weekday()]} {now.day} {data[now.month]} {now.year} года     {now.hour}:{now.minute}')


bot.polling()