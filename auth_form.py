# auth_form.py

import tkinter as tk
from tkinter import ttk

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
        self.correct_login = ""
        self.correct_password = ""

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

        # Опция для минимальной высоты строки
        self.auth_frame.grid_rowconfigure(0, weight=1)
        self.auth_frame.grid_rowconfigure(1, weight=1)
        self.auth_frame.grid_rowconfigure(2, weight=1)

    def set_login_success_callback(self, callback):
        self.login_success_callback = callback

    def login(self):
        # Метод для обработки входа
        login = self.entry_login.get()
        password = self.entry_password.get()
        if login == self.correct_login and password == self.correct_password:
            print("Успешная авторизация!")
            self.auth_frame.destroy()
            # Вызываем callback-функцию при успешной авторизации
            if self.login_success_callback:
                self.login_success_callback()
        else:
            print("Ошибка авторизации. Пожалуйста, проверьте введенные данные.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AuthForm(root)
    root.mainloop()
