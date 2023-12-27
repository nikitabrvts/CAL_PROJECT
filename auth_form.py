import tkinter as tk
from tkinter import ttk
import bcrypt

import psycopg2
from blocks import Blocks
from director_page import ManagerPage
from client_registrator import ClientRegistrator
from manager_reg_frame import RegistrationFrame

class AuthForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторизация")
        self.login_success_callback = None  # Callback-функция при успешной авторизации

        # Создаем стиль для виджетов ttk
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")  # Цвет фона для блока
        style.configure("TLabel", background="#f0f0f0")  # Цвет фона для меток
        style.configure("TEntry", background="#ffffff")  # Цвет фона для полей ввода
        style.configure("TButton", background="#a0a033")  # Цвет фона для кнопки

        # Задаем правильный логин и пароль для проверки
        self.correct_boss_login = "BOSS"
        self.correct_login = "SLAVE"
        self.correct_password = ""


        self.conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123"
        )

        self.cursor = self.conn.cursor()

        # Блок авторизации
        self.auth_frame = ttk.Frame(root, style="TFrame")
        self.auth_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.auth_frame, text="Авторизация", style="TLabel").grid(row=0, column=0, pady=5)

        ttk.Label(self.auth_frame, text="Логин:", style="TLabel").grid(row=1, column=0, pady=5)
        self.entry_login = ttk.Entry(self.auth_frame, style="TEntry")
        self.entry_login.grid(row=1, column=1, pady=5)

        ttk.Label(self.auth_frame, text="Пароль:", style="TLabel").grid(row=2, column=0, pady=5)
        self.entry_password = ttk.Entry(self.auth_frame, show="*", style="TEntry")
        self.entry_password.grid(row=2, column=1, pady=5)

        ttk.Button(self.auth_frame, text="Войти", command=self.login, style="TButton").grid(row=3, column=0, columnspan=2, pady=10)
        ttk.Button(self.auth_frame, text="Регистрация", command=self.registration, style="TButton").grid(row=4, column=0, columnspan=2, pady=10)

        # Опция для минимальной высоты строки
        self.auth_frame.grid_rowconfigure(0, weight=1)
        self.auth_frame.grid_rowconfigure(1, weight=1)
        self.auth_frame.grid_rowconfigure(2, weight=1)

    def set_login_success_callback(self, callback):
        self.login_success_callback = callback
    def registration(self):
        self.auth_frame.destroy()
        self.registration_page = RegistrationFrame(self.root)
    
    
    def login(self):
        # Метод для обработки входа
        login = self.entry_login.get()
        password = self.entry_password.get()

        # Получаем хэш пароля из базы данных
        self.cursor.execute("SELECT password_hash FROM authorisation WHERE login=%s", (login,))
        result = self.cursor.fetchone()
        print(result[0])

        if result:
            hashed_password_from_db = result[0]
            # Ensure that hashed_password_from_db is of type bytes
            if isinstance(hashed_password_from_db, str):
                hashed_password_from_db = hashed_password_from_db.encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password_from_db) and login != "BOSS":
                print("Успешная авторизация!")
                self.auth_frame.destroy()
                self.blocks_page = ClientRegistrator(self.root)
                # Вызываем callback-функцию при успешной авторизации
                if self.login_success_callback:
                    self.login_success_callback()
            elif  bcrypt.checkpw(password.encode('utf-8'), hashed_password_from_db) and login == "BOSS":
                print("Успешная авторизация БОССА!")
                self.auth_frame.destroy()
                # Создаем экземпляр ManagerPage
                self.manager_page = ManagerPage(self.root)
                # Вызываем метод show_page для отображения страницы руководителя
                self.manager_page.show_page()
                # Вызываем callback-функцию при успешной авторизации
                if self.login_success_callback:
                    self.login_success_callback()
            else:
                print("Неверный пароль.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AuthForm(root)
    root.mainloop()
