import sqlite3

# Создаем подключение к базе данных (если базы данных не существует, она будет создана)
conn = sqlite3.connect("project_database.db")

# Создаем объект-курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Создаем таблицу clients
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        middle_name TEXT,
        phone_number TEXT,
        contract_number TEXT,
        review TEXT
    )
''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()
