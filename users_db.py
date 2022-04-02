import config
import sqlite3


# @config.bot.message_handler(commands=['st'])
def start_registration(message):
    connect = sqlite3.connect('users_from_tg.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users_id(
        id,
        first_name,
        last_name        
    )""")
    connect.commit()

    user_info = [message.chat.id, message.chat.first_name, message.chat.last_name]
    cursor.execute("INSERT INTO users_id VALUES(?,?,?);", user_info)
    connect.commit()
