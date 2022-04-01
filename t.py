'''

git commit -a -m "example commit"

git push
'''

'''
кнопка нажимая на которую в бд добавляется имя пользователя нажавшего на нее.
Если имя уже есть, то выводится об этом сообщение.

кнопка нажав на которую ты из БД получаешь свое имя либо счетчик сообщений (сколько сообщений ты отправил)
'''

import telebot
import sqlite3

bot = telebot.TeleBot('5165289525:AAHXivKdtmC7fsAdkWqae8PBkSVK-xQh-og')


@bot.message_handler(commands=['st'])
def start(message):
    connect = sqlite3.connect('users_from_tg.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users_id(
        id,
        first_name,
        last_name,
        nickname
    )""")

    connect.commit()

    user_info = [message.chat.id, message.chat.first_name, message.chat.last_name, message.chat.nickname]
    cursor.execute("INSERT INTO users_id VALUES(?,?,?,?);", user_info)
    connect.commit()
