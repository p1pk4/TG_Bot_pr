from config import bot
from cosmo_bot_db import register_user
from telebot import types


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
    button5 = types.InlineKeyboardButton('ffffffffffff')
    register_button = types.InlineKeyboardButton('💥 Регистрация 💥')

    markup.add(button2, button3, button4, button5, register_button)
    bot.send_message(message.chat.id, 'Hey, {0.first_name}!'.format(message.from_user), reply_markup=markup)


# def register_button(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     register_button = types.InlineKeyboardButton('💥 Регистрация 💥')
#     markup.add(register_button)
#     bot.send_message(message.chat.id, 'register start', reply_markup=markup)
#     # register_user()
