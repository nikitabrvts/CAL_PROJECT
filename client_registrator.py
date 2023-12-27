import tkinter as tk
from tkinter import ttk
from blocks import Blocks
import psycopg2
import uuid
from feedback import Feedback


class ClientRegistrator:
    def __init__(self, root):
        self.root = root
        self.feedback_instance = Feedback(self.root)

        self.root.title("Информация о клиенте")

        # Подключаемся к базе даннх


        self.conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123"
        )

        self.cursor = self.conn.cursor()

        # Создаем блок "Информация о клиенте"
        self.client_frame = ttk.Frame(root, style="TFrame")
        self.client_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.client_frame, text="Информация о клиенте", style="TLabel").grid(row=0, column=0, columnspan=2, pady=5)

        # Поля ввода
        ttk.Label(self.client_frame, text="Фамилия:").grid(row=1, column=0, pady=5)
        self.entry_last_name = ttk.Entry(self.client_frame)
        self.entry_last_name.grid(row=1, column=1, pady=5)

        ttk.Label(self.client_frame, text="Имя:").grid(row=2, column=0, pady=5)
        self.entry_first_name = ttk.Entry(self.client_frame)
        self.entry_first_name.grid(row=2, column=1, pady=5)

        ttk.Label(self.client_frame, text="Отчество:").grid(row=3, column=0, pady=5)
        self.entry_middle_name = ttk.Entry(self.client_frame)
        self.entry_middle_name.grid(row=3, column=1, pady=5)

        ttk.Label(self.client_frame, text="Телефон:").grid(row=4, column=0, pady=5)
        self.entry_phone = ttk.Entry(self.client_frame)
        self.entry_phone.grid(row=4, column=1, pady=5)

        # Кнопка "Перейти к расчету"
        ttk.Button(self.client_frame, text="Перейти к расчету", command=self.register_client).grid(row=5, column=0, columnspan=2, pady=10)
        # Кнопка "Обратная связь"        
        ttk.Button(self.client_frame, text="Обратная связь", command=self.go_to_feedback_page).grid(row=6, column=0, columnspan=2, pady=10)

        # Опция для минимальной высоты строки
        self.client_frame.grid_rowconfigure(0, weight=1)

        # Генерируем уникальный номер договора
        self.contract_number = str(uuid.uuid4())


    def go_to_feedback_page(self):
        self.client_frame.destroy()
        self.feedback_instance


    def register_client(self):
        # Получаем данные из полей ввода
        last_name = self.entry_last_name.get()
        first_name = self.entry_first_name.get()
        middle_name = self.entry_middle_name.get()
        phone = self.entry_phone.get()

        self.cursor.execute("INSERT INTO client (name, surname, middle_name, phone_number) VALUES (%s, %s, %s, %s)",
                            (last_name, first_name, middle_name, phone))
        self.conn.commit()
        # Закрываем соединение
        self.conn.close()

        # Переходим к расчету (ваш код)
        print("Переход к расчету для клиента:", first_name, last_name, "контракт № ", self.contract_number)

        self.client_frame.destroy()
        self.blocks_page = Blocks(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClientRegistrator(root)
    root.mainloop()
