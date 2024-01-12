import tkinter as tk
from tkinter import ttk
from blocks import Blocks
import psycopg2
import uuid
from feedback import Feedback
from psycopg2 import sql


class ClientRegistrator:
    def __init__(self, root):
        self.root = root
        #self.feedback_instance = Feedback(self.root)

        self.root.title("Информация о клиенте")

        # Создаем блок "Менеджер"
        self.contract_frame = ttk.Frame(root, style="TFrame")
        self.contract_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.contract_frame, text="Ответственный менеджер", style="TLabel").grid(row=0, column=0, columnspan=2, pady=5)
        # Поля ввода
        ttk.Label(self.contract_frame, text="ID сотрудника:").grid(row=1, column=0, pady=5)
        self.entry_manager_id = ttk.Entry(self.contract_frame)
        self.entry_manager_id.grid(row=1, column=1, pady=5)


        # Создаем блок "Информация о клиенте"
        self.client_frame = ttk.Frame(root, style="TFrame")
        self.client_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

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

        ttk.Label(self.client_frame, text="Почта:").grid(row=5, column=0, pady=5)
        self.entry_email = ttk.Entry(self.client_frame)
        self.entry_email.grid(row=5, column=1, pady=5)


        # Кнопка "Перейти к расчету"
        ttk.Button(self.client_frame, text="Перейти к расчету", command=self.register_client).grid(row=6, column=0, columnspan=2, pady=10)
        # Кнопка "Обратная связь"        
        ttk.Button(self.client_frame, text="Обратная связь", command=self.go_to_feedback_page).grid(row=7, column=0, columnspan=2, pady=10)

        # Опция для минимальной высоты строки
        self.client_frame.grid_rowconfigure(0, weight=1)

        # Генерируем уникальный номер договора
        self.contract_number = str(uuid.uuid4())


    def go_to_feedback_page(self):
        self.client_frame.destroy()
        self.contract_frame.destroy()
        self.feedback_instance = Feedback(self.root)



    def register_client(self):
        # Получаем данные из полей ввода
        first_name = self.entry_first_name.get()
        middle_name = self.entry_middle_name.get()
        last_name = self.entry_last_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        manager_id = self.entry_manager_id.get()

        # Подключение к базе данных PostgreSQL 
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="123"
        )
        cursor = connection.cursor()

        # SQL-запрос для вставки данных пользователя в таблицу
        query = "INSERT INTO client (name, surname, middle_name, phone_number, email) VALUES (%s, %s, %s, %s, %s);"

        # Выполнение SQL-запроса
        cursor.execute(query, (first_name, last_name, middle_name, phone, email))

        # Применение изменений в базе данных
        connection.commit()


        # SQL-запрос для получения id клиента по заданным параметрам
        query = "SELECT client_id FROM client WHERE surname = %s AND name = %s AND middle_name = %s AND phone_number = %s;"
        cursor.execute(query, (last_name, first_name, middle_name, phone))

        # Получаем результат запроса
        result = cursor.fetchone()

        result = (result[0]) 

        query = "INSERT INTO contract (client_id, manager_id) VALUES (%s, %s);"
        cursor.execute(query, (result, manager_id))
        connection.commit()
        query = "SELECT MAX(contract_id) FROM contract WHERE client_id = %s;"
        cursor.execute(query, (result,))
        result = cursor.fetchone()
        result = (result[0]) 




        # Закрытие соединения
        connection.close()
        self.contract_frame.destroy()
        self.client_frame.destroy()

        self.blocks_page = Blocks(self.root, result)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClientRegistrator(root)
    root.mainloop()
