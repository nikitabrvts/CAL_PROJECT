import tkinter as tk
from tkinter import ttk
import sqlite3

class ManagerPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Страница руководителя")
        self.show_page()

    def show_page(self):

        self.clients_data = self.fetch_clients_data()


        # Создаем блок "Клиенты"
        self.clients_frame = ttk.Frame(self.root, style="TFrame")
        self.clients_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.clients_frame, text="Клиенты", style="TLabel").grid(row=0, column=0, columnspan=5, pady=5)

        # Выводим информацию о клиентах
        for i, client in enumerate(self.clients_data, start=1):
            ttk.Label(self.clients_frame, text=f"Клиент {i}:", style="TLabel").grid(row=i, column=0, pady=5)
            ttk.Label(self.clients_frame, text=f"{client['first_name']}").grid(row=i, column=1, pady=5)
            ttk.Label(self.clients_frame, text=f"{client['last_name']}").grid(row=i, column=2, pady=5)
            ttk.Label(self.clients_frame, text=f"Договор: захуярь меня из базы").grid(row=i, column=3, pady=5)
            ttk.Label(self.clients_frame, text=f"Телефон: {client['phone_number']}").grid(row=i, column=4, pady=5)
            ttk.Label(self.clients_frame, text=f"Отзыв: {client['review']}").grid(row=i, column=5, pady=5)
            


            # Кнопка "Сформировать отчет" для каждого клиента
            ttk.Button(self.clients_frame, text="Сформировать отчет", command=lambda c=client: self.generate_report(c)).grid(row=i, column=5, pady=5)

        # Опция для минимальной высоты строки
        self.clients_frame.grid_rowconfigure(0, weight=1)

    
    def fetch_clients_data(self):
        # Метод для получения данных о клиентах из базы данных
        conn = sqlite3.connect("project_database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name, phone_number, review FROM clients")
        clients_data = [{'first_name': row[0], 'last_name': row[1], 'phone_number': row[2], 'review': row[3]} for row in cursor.fetchall()]
        conn.close()
        return clients_data

    def generate_report(self, client):
        # Метод для формирования отчета для выбранного клиента (ваш код здесь)
        print(f"Формирование отчета для клиента {client['Имя']} {client['Фамилия']}...")

if __name__ == "__main__":
    root = tk.Tk()
    app = ManagerPage(root)
    root.mainloop()
