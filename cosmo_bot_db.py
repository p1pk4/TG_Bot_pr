import sqlite3


# Коннект к БД
db = sqlite3.connect('cosmo_bot.db')
# Работа с БД (CRUD операции)
sql = db.cursor()

# Создать таблицу если она не создана 
sql.execute('''CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    count_message BIGINT
)''')
# Подтверждаем изменения в БД
db.commit()

user_login = input('Login: ')
user_password = input('Password: ')
count_message = 0

def register_user():
    ''' Если запись в БД уже есть, то мы не записываем туда данные. Если записи нет, то записываем в БД '''
    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        sql.execute("INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        db.commit()
        print('Логин и пароль записаны в базу данных!')
    else:
        print('Такой логин уже есть в базе данных!')
        for value in sql.execute("SELECT * FROM users"):
            print(value)

register_user()