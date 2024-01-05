import tkinter as tk
from tkinter import Canvas, ttk
from PyPDF2 import PdfMerger
import psycopg2
from psycopg2 import sql
from reportlab.pdfgen import canvas
from pdf_merger import PDFMerger


from time_to_payback import PaybackCalculator
from visitors_generator import VisitorsGenerator

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
            ttk.Label(self.clients_frame, text=f" {i}.", style="TLabel").grid(row=i, column=0, pady=5)
            ttk.Label(self.clients_frame, text=f"{client['first_name']}").grid(row=i, column=1, pady=5)
            ttk.Label(self.clients_frame, text=f"{client['last_name']}").grid(row=i, column=2, pady=5)
            ttk.Label(self.clients_frame, text=f"Договор: {client['contract_id']}").grid(row=i, column=3, pady=5)
            ttk.Label(self.clients_frame, text=f"Телефон: {client['phone_number']}").grid(row=i, column=4, pady=5)
            ttk.Label(self.clients_frame, text=f"Почта: {client['email']}").grid(row=i, column=5, pady=5)
            
            # Кнопка "Сформировать отчет" для каждого клиента
            ttk.Button(self.clients_frame, text="Сформировать отчет", command=lambda c=client: self.generate_report(c['contract_id'])).grid(row=i, column=6, pady=5)
            # Кнопка "Сформировать отчет" для каждого клиента
            ttk.Button(self.clients_frame, text="Посмотреть отзыв", command=lambda c=client: self.show_review(c['contract_id'])).grid(row=i, column=7, pady=5)

        # Опция для минимальной высоты строки
        self.clients_frame.grid_rowconfigure(0, weight=1)

    
    def fetch_clients_data(self):
        # Подключение к базе данных PostgreSQL (замените параметры подключения своими)
        self.connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123"
        )
        self.cursor = self.connection.cursor()   

        self.cursor.execute("SELECT name, surname, phone_number, email, contract_id FROM client JOIN contract ON client.client_id=contract.client_id")
        clients_data = [{'first_name': row[0], 'last_name': row[1], 'phone_number': row[2], 'email': row[3],  'contract_id': row[4]} for row in self.cursor.fetchall()]
        return clients_data
    
    def fetch_contract_data(self, contract_id):
        query = "SELECT * FROM contract WHERE contract_id = %s;"
        self.cursor.execute(query, (contract_id,))
        contract_data = self.cursor.fetchall()
        return contract_data
    
    def fetch_invested_data(self, contract_id):
        query = "SELECT * FROM invested WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        invest_data = self.cursor.fetchall()
        total_invest = sum(invest_data[0]) - contract_id
        return total_invest
    def fetch_income_data(self, contract_id):
        query = "SELECT * FROM income WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        income_data = self.cursor.fetchall()
        input_numbers = [income_data[0][2], income_data[1][2], income_data[2][2], income_data[3][2], income_data[4][2]]
        generator = VisitorsGenerator()
        visitors_list = generator.generate_visitors(input_numbers)
        print(len(visitors_list))
        result_list = [x * income_data[0][3] for x in visitors_list]
        return result_list
    def fetch_expens_data(self, contract_id):
        query = "SELECT * FROM expenses WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        expens_data = self.cursor.fetchall()
        total_expens_data = sum(expens_data[0]) - contract_id 
        return total_expens_data
    def fetch_review_data(self, contract_id):
        query = "SELECT * FROM review WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        review = self.cursor.fetchall()
        return review[0][2]
    
    

    def generate_report(self, client):
        # Метод для формирования отчета для выбранного клиента (ваш код здесь)
        print(f"Формирование отчета для клиента...", client)
        payback = PaybackCalculator(
            int(app.fetch_invested_data(client)),
            app.fetch_income_data(client),
            int(app.fetch_expens_data(client))
                )
        payback.plot_payback_graph()
        payback.plot_profit_graph()

        self.write_variables_to_pdf("1.pdf", payback.initial_budget, payback.payback_time_months )

        pdf_merger = PdfMerger()# Добавляем PDF-файлы
        pdf_merger.append('1.pdf')
        pdf_merger.append('payback_graph.pdf')
        pdf_merger.append('profit_graph.pdf')

        # Сохраняем объединенный PDF
        result_filename = 'RESULT_FOR_CONTRACT_{}.pdf'.format(client)
        with open(result_filename, 'wb') as output_pdf:
            pdf_merger.write(output_pdf)


    def show_review(self, client):
        # Метод для формирования отчета для выбранного клиента (ваш код здесь)
        print(f"Формирование отзыва от клиента...")
        review = self.fetch_review_data(client)
        print (review)
        self.write_variables_to_pdf("review.pdf", review, client )




    def write_variables_to_pdf(self, filename, variable1, variable2):
    # Создаем PDF-документ
        pdf_canvas = canvas.Canvas(filename)
    # Записываем значения переменных в PDF
        pdf_canvas.drawString(100, 800, f"I CAN SAY ABOUT COMPANY: {variable1}")
        pdf_canvas.drawString(100, 780, f"REVIEW FROM CLIENT: {variable2}")
    # Закрываем PDF-документ
        pdf_canvas.save()


if __name__ == "__main__":
    root = tk.Tk()
    app = ManagerPage(root)
#    print("help")
#    print(app.fetch_invested_data(26))
#    print(app.fetch_expens_data(26))
#    print(app.fetch_income_data(26))
#    payback = PaybackCalculator(app.fetch_invested_data(26), app.fetch_income_data(26), app.fetch_expens_data(26))
#    print(payback.calculate_payback_time())
#
#    payback1 = PaybackCalculator(
#        int(app.fetch_invested_data(26)),
#        app.fetch_income_data(26),
#        int(app.fetch_expens_data(26))
#        )
#    payback1.plot_payback_graph()
#    payback1.plot_profit_graph()







    root.mainloop()
