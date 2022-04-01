from telebot import types
from config import bot


# Список для логов
user_logs = []


# Старт бота с функциями кнопок
@bot.message_handler(commands=["start"])
def start(message, res=False):
    url_youtube_button(message)
    buttons_menu(message)
    url_vk_button(message)

def url_youtube_button(message):
     '''URL кнопка'''
     markup = types.InlineKeyboardMarkup()
     url_button = types.InlineKeyboardButton('YouTube', url='https://www.youtube.com/watch?v=n0Zli_fQeP8')
     markup.add(url_button)
     bot.send_message(message.chat.id, 'Привет, {0.first_name}! Нажми на кнопку'.format(message.from_user),
                      reply_markup=markup)

def url_vk_button(message):
     '''URL кнопка'''
     markup = types.InlineKeyboardMarkup()
     url_button = types.InlineKeyboardButton('VK', url='https://www.vk.com/feed')
     markup.add(url_button)
     bot.send_message(message.chat.id, 'Привет, {0.first_name}! Нажми на кнопку'.format(message.from_user),
                      reply_markup=markup)

def buttons_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.InlineKeyboardButton('💥 Регистрация 💥')

    button2 = types.InlineKeyboardButton('🤖 Группа в ВКонтакте 🤖')

    button3 = types.InlineKeyboardButton('❤ Магазин ❤')

    button4 = types.InlineKeyboardButton('💌 Обратная связь 💌')

    button5 = types.InlineKeyboardButton('ffffffffffff')

    markup.add(button1, button2, button3, button4, button5)

    bot.send_message(message.chat.id, 'Hey, {0.first_name}!'.format(message.from_user), reply_markup=markup)


# # Эхо(копия) сообщений от пользователя
# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
#     logs(message)


# Запись логов в файл
def logs(message):
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write('\n' + str(message.from_user.username) + ': ' + message.text)


# Запуск бота
bot.polling(none_stop=True, interval=0)