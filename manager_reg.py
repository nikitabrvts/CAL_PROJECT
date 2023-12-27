import bcrypt
import psycopg2
from psycopg2 import sql


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def hash_password(self):
        # Генерация хэша пароля с использованием соли
        return bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())

    def register_user(self):
        # Подключение к базе данных PostgreSQL (замените параметры подключения своими)
        connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123"
        )
        cursor = connection.cursor()

        # Генерация хэша пароля
        hashed_password = self.hash_password()

        # SQL-запрос для вставки данных пользователя в таблицу
        query = sql.SQL("INSERT INTO authorisation (login, password_hash) VALUES ({}, {});").format(
            sql.Literal(self.login),
            sql.Literal(hashed_password.decode('utf-8'))  # Преобразование bytes в строку
        )

        # Выполнение SQL-запроса
        cursor.execute(query)

        # Применение изменений в базе данных
        connection.commit()

        # Закрытие соединения
        connection.close()

if __name__ == "__main__":
    # Пример использования класса Registration
    registration = Registration(login="1", password="1")
    registration.register_user()
