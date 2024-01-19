import tkinter as tk
from tkinter import Canvas, ttk
from tkinter import messagebox
from PyPDF2 import PdfMerger
import psycopg2
from psycopg2 import sql
from reportlab.pdfgen import canvas
from pdf_merger import PDFMerger
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics



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
    
    def fetch_fio_data(self, contract_id):
        query = "SELECT * FROM contract WHERE contract_id = %s;"
        self.cursor.execute(query, (contract_id,))
        contract_data = self.cursor.fetchall()

        query = "SELECT * FROM client WHERE client_id = %s;"
        self.cursor.execute(query, (contract_data[0][1],))
        fio_data = self.cursor.fetchall()
        return fio_data

    def fetch_invested_data(self, contract_id):
        query = "SELECT * FROM invested WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        invest_data = self.cursor.fetchall()
        total_invest1 = invest_data[0][1] + invest_data[0][2] + invest_data[0][3] + invest_data[0][4] + invest_data[0][5] 
        total_invest = total_invest1 + invest_data[0][6] + invest_data[0][7] + invest_data[0][8] + invest_data[0][9] + invest_data[0][10] 
        return total_invest
    
    def fetch_all_invested_data(self, contract_id):
        query = "SELECT * FROM invested WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        invest_data = self.cursor.fetchall()
        return invest_data  
      
    def fetch_income_data(self, contract_id):
        query = "SELECT * FROM income WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        income_data = self.cursor.fetchall()
        input_numbers = [income_data[0][2], income_data[1][2], income_data[2][2], income_data[3][2], income_data[4][2]]
        generator = VisitorsGenerator()
        visitors_list = generator.generate_visitors(input_numbers)
        result_list = [x * income_data[0][3] for x in visitors_list]
        return result_list
    
    def fetch_expens_data(self, contract_id):
        query = "SELECT * FROM expenses WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        expens_data = self.cursor.fetchall()
        #total_expens_data = sum(expens_data[0]) - contract_id 
        #total_expens_data = sum(row[1:] for row in expens_data)
        total_expens_data = int(expens_data[0][1]) + int(expens_data[0][2]) + int(expens_data[0][3]) + int(expens_data[0][4]) + int(expens_data[0][5]) + int(expens_data[0][6]) + int(expens_data[0][7])
        return total_expens_data

    def fetch_expens_dat_detailed(self, contract_id):
        query = "SELECT * FROM expenses WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        expens_data = self.cursor.fetchall()
        return expens_data

    def fetch_review_data(self, contract_id):
        query = "SELECT * FROM review WHERE contract_id = %s ORDER BY review_id DESC LIMIT 1;"
        self.cursor.execute(query, ([contract_id]))
        review = self.cursor.fetchall()
        return review[0][2]
    def fetch_check_data(self, contract_id):
        query = "SELECT * FROM income WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        income_data = self.cursor.fetchall()
        return income_data
    
    def fetch_income_data_av(self, contract_id):
        query = "SELECT * FROM income WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        income_data = self.cursor.fetchall()
        input_numbers = [income_data[0][2], income_data[1][2], income_data[2][2], income_data[3][2], income_data[4][2]]
        generator = VisitorsGenerator()
        visitors_list = generator.generate_visitors(input_numbers)
        sum_of_list = 0
        for i in range(len(visitors_list)):
            sum_of_list += int(visitors_list[i])
        average = int(sum_of_list/len(visitors_list))
        return average
    
    def generate_report(self, client):
        # Метод для формирования отчета для выбранного клиента (ваш код здесь)
        #print(f"Формирование отчета для клиента...", client)

        payback = PaybackCalculator(
            int(app.fetch_invested_data(client))*1.15,
            app.fetch_income_data(client),
            int(app.fetch_expens_data(client))
                )
        payback1 = PaybackCalculator(
            int(app.fetch_invested_data(client))*1.15,
            app.fetch_income_data(client),
            int(app.fetch_expens_data(client))
                )
        self.month = payback1.calculate_payback_time()
        self.invested_data = app.fetch_all_invested_data(client)
        self.about_inv_data = app.fetch_invested_data(client)
        self.income_data = app.fetch_income_data(client)
        self.expense_data = app.fetch_expens_data(client)
        self.contract = app.fetch_contract_data(client)
        self.fio = app.fetch_fio_data(client)
        self.check = app.fetch_check_data(client)
        self.av = app.fetch_income_data_av(client)
        self.e = app.fetch_expens_dat_detailed(client)
    # Создаем PDF-документ
        font_path = 'Arial.ttf'
    
    # Создаем PDF-документ с указанием шрифта
        pdf_canvas = canvas.Canvas("repo.pdf", pagesize=letter)

        pdfmetrics.registerFont(TTFont('FreeSans', 'arial.ttf'))
        pdf_canvas.setFont('FreeSans', 12)

        pdf_canvas.drawString(125, 760, f"Информация о договоре:")
        
        pdf_canvas.drawString(100, 740, f"Информация о клиенте:{self.fio[0][1]}, {self.fio[0][2]}, {self.fio[0][3]}, {self.fio[0][4]}  ")
        pdf_canvas.drawString(100, 720, f"Номер договора: {self.contract[0][0]}")
        pdf_canvas.drawString(100, 700, f"Идентификатор менеджера: {self.contract[0][2]}")


        pdf_canvas.drawString(125, 660, f"Расходы до открытия: ")

        pdf_canvas.drawString(100, 640, f"Аренда: {self.invested_data[0][1]}")
        pdf_canvas.drawString(100, 620, f"Ремонт: {self.invested_data[0][2]}")
        pdf_canvas.drawString(100, 600, f"Оборудование: {self.invested_data[0][3]}")
        pdf_canvas.drawString(100, 580, f"Продукты: {self.invested_data[0][4]}")
        pdf_canvas.drawString(100, 560, f"Документооборот: {self.invested_data[0][5]}")
        pdf_canvas.drawString(100, 540, f"ФОТ: {self.invested_data[0][6]}")
        pdf_canvas.drawString(100, 520, f"Услуги охранной организации: {self.invested_data[0][7]}")
        pdf_canvas.drawString(100, 500, f"Маркетинг: {self.invested_data[0][8]}")
        pdf_canvas.drawString(100, 480, f"Коммунальные платежы: {self.invested_data[0][9]}")
        pdf_canvas.drawString(100, 460, f"Налоги: {self.invested_data[0][10]}")

        pdf_canvas.drawString(125, 420, f"Гости и средний чек:")

        pdf_canvas.drawString(100, 400, f"Среднее предполагаемое количество гостей: {int(self.check[4][2])}")
        pdf_canvas.drawString(100, 380, f"Средний чек: {int(self.check[0][3])}")

        pdf_canvas.drawString(125, 340, f"Ежемесячные расходы:")

        pdf_canvas.drawString(100, 320, f"Ежемесячная аренда: {self.e[0][2]}")
        pdf_canvas.drawString(100, 300, f"Ремонт: {self.e[0][3]}")
        pdf_canvas.drawString(100, 280, f"Продукты: {self.e[0][4]}")
        pdf_canvas.drawString(100, 260, f"Зароботная плата: {self.e[0][5]}")
        pdf_canvas.drawString(100, 240, f"Услуги охранной организации: {self.e[0][6]}")
        pdf_canvas.drawString(100, 220, f"Маркетинг: {self.e[0][7]}")
        pdf_canvas.drawString(100, 200, f"Коммунальные платежи: {self.e[0][8]}")


        pdf_canvas.drawString(125, 160, f"Первоначальные инвестиции и срок окупаемости:")

        pdf_canvas.drawString(100, 140, f"Сумма первоначальных инвестиций: {self.about_inv_data * 1.15}")
        pdf_canvas.drawString(100, 120, f"Срок окупаемости (мес.): {self.month - 2}")



        pdf_canvas.save()            

        payback.plot_payback_graph()
        payback.plot_profit_graph()

        pdf_merger = PdfMerger()# Добавляем PDF-файлы
        pdf_merger.append('repo.pdf')
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
        self.write_variables_to_txt("review.doc", review, client )
        messagebox.showinfo("", f"{review}\n\n\n Копия отзыва сохранена на вашем компьютере!")

    def write_variables_to_txt(self, filename, variable1, variable2):
    # Открываем файл для записи
        with open(filename, 'w', encoding='utf-8') as txt_file:
        # Записываем значения переменных в файл
            txt_file.write(f"Отзыв от клиента с договором №: {variable2}\n")
            txt_file.write(f"Что я могу сказать о проделанной работе: {variable1}\n")
            

if __name__ == "__main__":
    root = tk.Tk()
    app = ManagerPage(root)
    root.mainloop()
