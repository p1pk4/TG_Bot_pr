import telebot
from telebot import types
import cosmo_bot_db
from cosmo_bot_db import register_user

# Экземпляр бота
bot = telebot.TeleBot('5165289525:AAESx2TR6E6olvLS13ysS5kU9ere8KRNt14')

# Список для логов
user_logs = []


# Старт бота с функциями кнопок
@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, 'First message from bot')
    url_button(message)
    register_user()


def url_button(message):
    '''URL кнопка'''
    markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton('youtube', url='https://youtube.com')
    markup.add(url_button)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}! Нажми на кнопку'.format(message.from_user),
                     reply_markup=markup)


# Эхо(копия) сообщений от пользователя
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
    logs(message)


# Запись логов в файл
def logs(message):
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write('\n' + str(message.from_user.username) + ': ' + message.text)


# Запуск бота
bot.polling(none_stop=True, interval=0)