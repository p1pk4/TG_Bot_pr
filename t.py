import telebot
from telebot import types # для указание типов
import config

bot = telebot.TeleBot('5165289525:AAESx2TR6E6olvLS13ysS5kU9ere8KRNt14')

@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Сайт Хабр", url='https://www.youtube.com/')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)
bot.polling(none_stop=True)