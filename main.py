from bot_buttons import *
from users_db import start_registration


# Список для логов
user_logs = []


# Старт бота с функциями кнопок
@bot.message_handler(commands=["start"])
def start(message, res=False):
    url_youtube_button(message)
    url_git_project_button(message)
    buttons_menu(message)
    register_button(message)
    start_registration(message)
    random_button(message)


# Запись логов в файл
def logs(message):
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write('\n' + str(message.from_user.username) + ': ' + message.text)


# Запуск бота
bot.polling(none_stop=True, interval=0)
