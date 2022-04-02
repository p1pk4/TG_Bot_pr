import random

from config import bot
from telebot import types
from users_db import start_registration


def url_youtube_button(message):
    """URL кнопка"""
    markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton('YouTube', url='https://www.youtube.com/watch?v=n0Zli_fQeP8')
    markup.add(url_button)
    bot.send_message(message.chat.id, 'YouTube', reply_markup=markup)


def url_git_project_button(message):
    """URL кнопка"""
    markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton('Github Project', url='https://github.com/p1pk4/TG_Bot_pr')
    markup.add(url_button)
    bot.send_message(message.chat.id, 'Ссылка на проект', reply_markup=markup)


def buttons_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button2 = types.InlineKeyboardButton('🤖 Группа в ВКонтакте 🤖')
    button3 = types.InlineKeyboardButton('❤ Магазин ❤')
    button4 = types.InlineKeyboardButton('💌 Обратная связь 💌')
    rand_button = types.InlineKeyboardButton('Random number')
    reg_button = types.InlineKeyboardButton('Регистрация')

    markup.add(button2, button3, button4, rand_button, reg_button)
    bot.send_message(message.chat.id, 'Hey, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def register_button(message):
    """ Когда пользователь нажимает на кнопку '💥 Регистрация 💥', его id добавляется в бд """
    if message.chat.type == 'private':
        if message.text == 'Регистрация':
            start_registration(message)
            bot.send_message(message.chat.id, 'Вы зарегистрировались в базе данных!')


def random_button(message):
    if message.chat.type == 'private':
        if message.text == 'Random number':
            bot.send_message(message.text, 'Your number: ' + str(random.randint(0, 1000)))
