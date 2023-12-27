import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from manager_reg import Registration

class RegistrationFrame:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")

        # Создаем фрейм
        self.registration_frame = ttk.Frame(root, padding=(20, 10))
        self.registration_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Добавляем поля для ввода
        ttk.Label(self.registration_frame, text="Логин:").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_login = ttk.Entry(self.registration_frame, width=20)
        self.entry_login.grid(row=0, column=1, pady=5)

        ttk.Label(self.registration_frame, text="Пароль:").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_password = ttk.Entry(self.registration_frame, show="*", width=20)
        self.entry_password.grid(row=1, column=1, pady=5)

        # Кнопка для регистрации
        ttk.Button(self.registration_frame, text="Создать нового пользователя", command=self.register_user).grid(row=2, column=0, columnspan=2, pady=10)

    def register_user(self):
        # Получаем введенные данные из полей
        login = self.entry_login.get()
        password = self.entry_password.get()

        # Проверяем, что логин и пароль не пустые
        if not login or not password:
            messagebox.showerror("Ошибка", "Пожалуйста, введите логин и пароль.")
            return

        # Создаем экземпляр класса Registration и регистрируем пользователя
        registration = Registration(login=login, password=password)
        registration.register_user()

        # Очищаем поля после регистрации
        self.entry_login.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

        # Выводим сообщение об успешной регистрации
        messagebox.showinfo("Успешно", "Регистрация прошла успешно!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationFrame(root)
    root.mainloop()
