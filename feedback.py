import tkinter as tk
from tkinter import ttk
import sqlite3

import psycopg2

class Feedback:
    def __init__(self, root):
    
        self.root = root
        self.root.title("Обратная связь")

        # Создаем блок "Обратная связь"
        self.feedback_frame = ttk.Frame(self.root, style="TFrame")
        self.feedback_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.feedback_frame, text="Блок \"Обратная связь\"", style="TLabel").grid(row=0, column=0, columnspan=2, pady=5)

        ttk.Label(self.feedback_frame, text="Номер договора:", style="TLabel").grid(row=1, column=0, pady=5)
        self.entry_contract_number = ttk.Entry(self.feedback_frame, style="TEntry")
        self.entry_contract_number.grid(row=1, column=1, pady=5)

        ttk.Label(self.feedback_frame, text="Отзыв:", style="TLabel").grid(row=2, column=0, pady=5)
        self.entry_review = ttk.Entry(self.feedback_frame, style="TEntry")
        self.entry_review.grid(row=2, column=1, pady=5)

        ttk.Button(self.feedback_frame, text="Отправить отзыв", command=self.send_feedback, style="TButton").grid(row=3, column=0, columnspan=2, pady=10)

        # Опция для минимальной высоты строки
        self.feedback_frame.grid_rowconfigure(0, weight=1)

    def send_feedback(self):
        # Метод для отправки отзыва
        contract_number = self.entry_contract_number.get()
        review = self.entry_review.get()

        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="123")
        cursor = connection.cursor()

        query = "INSERT INTO review (contract_id, text_review) VALUES (%s, %s);"
        cursor.execute(query, (contract_number, review))
        connection.commit()        
        connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = Feedback(root)
    root.mainloop()