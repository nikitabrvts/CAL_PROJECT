import tkinter as tk
from tkinter import Canvas, ttk
import psycopg2
from pdf_merger import PDFMerger
from time_to_payback import PaybackCalculator
from visitors_generator import VisitorsGenerator
from final_block import FinalBlock
from reportlab.pdfgen import canvas

class Blocks:
    def __init__(self, root, result):
        self.root = root
        self.result = result
        self.root.title("Блоки с данными")
        self.months =   0

        # Создаем стиль для виджетов ttk
        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")  # Цвет фона для блоков
        style.configure("TLabel", background="#f0f0f0")  # Цвет фона для меток
        style.configure("TEntry", background="#ffffff")  # Цвет фона для полей ввода

        # Блок "Первоначальные инвестиции"
        self.investment_frame = ttk.Frame(root, borderwidth=2, relief="solid", width=200, height=100)
        self.investment_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.investment_frame, text="Первоначальные инвестиции", style="TLabel").grid(row=0, column=0, pady=5)

        ttk.Label(self.investment_frame, text="Аренда", style="TLabel").grid(row=1, column=0, pady=10,  sticky="w", padx=5)
        self.entry_initial_rent = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_initial_rent.grid(row=1, column=1, pady=5)

        ttk.Label(self.investment_frame, text="Ремонт:", style="TLabel").grid(row=2, column=0, pady=10,  sticky="w", padx=5)
        self.entry_repair = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_repair.grid(row=2, column=1, pady=5)

        ttk.Label(self.investment_frame, text="Оборудование:", style="TLabel").grid(row=3, column=0, pady=10,  sticky="w", padx=5)
        self.entry_equipment = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_equipment.grid(row=3, column=1, pady=5)

        ttk.Label(self.investment_frame, text="Продукты:", style="TLabel").grid(row=4, column=0, pady=10,  sticky="w", padx=5)
        self.entry_products = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_products.grid(row=4, column=1, pady=5)

        ttk.Label(self.investment_frame, text="Документы:", style="TLabel").grid(row=5, column=0, pady=10,  sticky="w", padx=5)
        self.entry_documents = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_documents.grid(row=5, column=1, pady=5)

        ttk.Label(self.investment_frame, text="ФОТ:", style="TLabel").grid(row=6, column=0, pady=10,  sticky="w", padx=5)
        self.entry_fot = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_fot.grid(row=6, column=1, pady=5)

        ttk.Label(self.investment_frame, text="Охрана:", style="TLabel").grid(row=7, column=0, pady=10,  sticky="w", padx=5)
        self.entry_guard = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_guard.grid(row=7, column=1, pady=5)

        ttk.Label(self.investment_frame, text="Маркетинг:", style="TLabel").grid(row=8, column=0, pady=10,  sticky="w", padx=5)
        self.entry_smm = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_smm.grid(row=8, column=1, pady=5)

        ttk.Label(self.investment_frame, text="Коммунальные платежи:", style="TLabel").grid(row=9, column=0, pady=10,  sticky="w", padx=5)
        self.entry_service = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_service.grid(row=9, column=1, pady=5)

        ttk.Label(self.investment_frame, text="Налоги:", style="TLabel").grid(row=10, column=0, pady=10,  sticky="w", padx=5)
        self.entry_tax = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_tax.grid(row=10, column=1, pady=5)


        #
        #
        #
        #
        #

        # Опция для минимальной высоты строки
        self.investment_frame.grid_rowconfigure(0, weight=1)
        self.investment_frame.grid_rowconfigure(1, weight=1)
        self.investment_frame.grid_rowconfigure(2, weight=1)

        # Блок "Доходы"
        self.income_frame = ttk.Frame(root, borderwidth=2, relief="solid", width=200, height=100)
        self.income_frame.grid(row=1, column=0, padx=10, pady=10)

        ttk.Label(self.income_frame, text="Доходы", style="TLabel").grid(row=0, column=0, pady=5)

        ttk.Label(self.income_frame, text="Количество посетителей (1 мес.):", style="TLabel").grid(row=1, column=0, pady=5)
        self.entry_visitors1 = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_visitors1.grid(row=1, column=1, pady=5)

        ttk.Label(self.income_frame, text="Количество посетителей (2 мес.):", style="TLabel").grid(row=2, column=0, pady=5)
        self.entry_visitors2 = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_visitors2.grid(row=2, column=1, pady=5)        

        ttk.Label(self.income_frame, text="Количество посетителей (3 мес.):", style="TLabel").grid(row=3, column=0, pady=5)
        self.entry_visitors3 = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_visitors3.grid(row=3, column=1, pady=5)

        ttk.Label(self.income_frame, text="Количество посетителей (4 мес.):", style="TLabel").grid(row=4, column=0, pady=5)
        self.entry_visitors4 = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_visitors4.grid(row=4, column=1, pady=5)

        ttk.Label(self.income_frame, text="Количество посетителей (5 мес.):", style="TLabel").grid(row=5, column=0, pady=5)
        self.entry_visitors5 = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_visitors5.grid(row=5, column=1, pady=5)

        ttk.Label(self.income_frame, text="Средний чек:", style="TLabel").grid(row=6, column=0, pady=5,  sticky="w", padx=5)
        self.entry_average_check = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_average_check.grid(row=6, column=1, pady=5)

        # Опция для минимальной высоты строки
        self.income_frame.grid_rowconfigure(0, weight=1)
        self.income_frame.grid_rowconfigure(1, weight=1)
        self.income_frame.grid_rowconfigure(2, weight=1)

        #
        #
        #
        #
        #

        # Блок "Расходы"
        self.expenses_frame = ttk.Frame(root, borderwidth=2, relief="solid", width=200, height=100)
        self.expenses_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.expenses_frame, text="Расходы", style="TLabel").grid(row=0, column=0, pady=5)

        ttk.Label(self.expenses_frame, text="Аренда:", style="TLabel").grid(row=1, column=0, pady=10,  sticky="w", padx=5)
        self.entry_month_rent = ttk.Entry(self.expenses_frame, style="TEntry")
        self.entry_month_rent.grid(row=1, column=1, pady=5)

        ttk.Label(self.expenses_frame, text="Ремонт:", style="TLabel").grid(row=2, column=0, pady=10,  sticky="w", padx=5)
        self.entry_month_repair = ttk.Entry(self.expenses_frame, style="TEntry")
        self.entry_month_repair.grid(row=2, column=1, pady=5)

        ttk.Label(self.expenses_frame, text="Продукты:", style="TLabel").grid(row=3, column=0, pady=10,  sticky="w", padx=5)
        self.entry_month_products = ttk.Entry(self.expenses_frame, style="TEntry")
        self.entry_month_products.grid(row=3, column=1, pady=5)

        ttk.Label(self.expenses_frame, text="ФОТ:", style="TLabel").grid(row=4, column=0, pady=10,  sticky="w", padx=5)
        self.entry_month_fot = ttk.Entry(self.expenses_frame, style="TEntry")
        self.entry_month_fot.grid(row=4, column=1, pady=5)

        ttk.Label(self.expenses_frame, text="Охрана:", style="TLabel").grid(row=5, column=0, pady=10,  sticky="w", padx=5)
        self.entry_month_guard = ttk.Entry(self.expenses_frame, style="TEntry")
        self.entry_month_guard.grid(row=5, column=1, pady=5)

        ttk.Label(self.expenses_frame, text="Маркетинг:", style="TLabel").grid(row=6, column=0, pady=10,  sticky="w", padx=5)
        self.entry_month_smm = ttk.Entry(self.expenses_frame, style="TEntry")
        self.entry_month_smm.grid(row=6, column=1, pady=5)

        ttk.Label(self.expenses_frame, text="Коммунальные платежи:", style="TLabel").grid(row=7, column=0, pady=5, sticky="w", padx=5)
        self.entry_month_service = ttk.Entry(self.expenses_frame, style="TEntry")
        self.entry_month_service.grid(row=7, column=1, pady=5)

        # Опция для минимальной высоты строки
        self.expenses_frame.grid_rowconfigure(0, weight=1)
        self.expenses_frame.grid_rowconfigure(1, weight=1)
        self.expenses_frame.grid_rowconfigure(2, weight=1)

        # Опция для минимальной высоты строки
        root.grid_rowconfigure(3, weight=1)

        # Кнопка "Рассчитать"
        self.calculate_button = ttk.Button(root, text="вызов калькулятора", command=self.perform_calculations)
        self.calculate_button.grid(row=1, column=4, pady=10)
        
        # Опция для минимальной высоты строки
        root.grid_rowconfigure(3, weight=1)

    def perform_calculations(self):
        self.initial_rent = int(self.entry_initial_rent.get())
        self.repair = int(self.entry_repair.get())
        self.equipment = int(self.entry_equipment.get())
        self.products = int(self.entry_products.get())
        self.documents = int(self.entry_documents.get())
        self.fot = int(self.entry_fot.get())
        self.guard = int(self.entry_guard.get())
        self.smm = int(self.entry_smm.get())
        self.service = int(self.entry_service.get())
        self.tax = int(self.entry_tax.get())

        entry_v1 = self.entry_visitors1.get()
        entry_v2 = self.entry_visitors2.get()
        entry_v3 = self.entry_visitors3.get()
        entry_v4 = self.entry_visitors4.get()
        entry_v5 = self.entry_visitors5.get()
        av_check = int(self.entry_average_check.get())
        input_numbers = [entry_v1, entry_v2, entry_v3, entry_v4, entry_v5]
        generator = VisitorsGenerator()
        self.num_av_check = int(av_check)
        visitors_list = generator.generate_visitors(input_numbers)
        sum_of_list = 0
        for i in range(len(visitors_list)):
            sum_of_list += int(visitors_list[i])
        self.average = sum_of_list/len(visitors_list)
        self.result_list = [int(x) * self.num_av_check for x in visitors_list]

        entry_month_rent = self.entry_month_rent.get()
        entry_month_repair = self.entry_month_repair.get()
        entry_month_products = self.entry_month_products.get()
        entry_month_fot = self.entry_month_fot.get()
        entry_month_guard = self.entry_month_guard.get()
        entry_month_smm = self.entry_month_smm.get()
        entry_month_service= self.entry_month_service.get()
        self.expenses = int(entry_month_rent) + int(entry_month_guard) + int(entry_month_products) + int(entry_month_repair) + int(entry_month_fot) + int(entry_month_service) + int(entry_month_smm)



        self.calculate_button.destroy()
        self.write_invested_to_database()
        self.payback_task()
        self.write_variables_to_pdf("1.pdf", self.ivest, self.months )
        
        pdf_merger = PDFMerger("RESULT.pdf")
        pdf_merger.add_pdf("1.pdf")
        pdf_merger.add_pdf("payback_graph.pdf")
        pdf_merger.add_pdf("profit_graph.pdf")
        pdf_merger.merge_pdfs()

        



    def write_variables_to_pdf(self, filename, variable1, variable2):
    # Создаем PDF-документ
        pdf_canvas = canvas.Canvas(filename)
    # Записываем значения переменных в PDF
        pdf_canvas.drawString(100, 820, f"Initial investments and detailing:")

        pdf_canvas.drawString(100, 800, f"Initial investment: {variable1}")
        pdf_canvas.drawString(100, 780, f"Payback period: {variable2}")
        pdf_canvas.drawString(100, 760, f"Initial rent: {self.initial_rent}")
        pdf_canvas.drawString(100, 740, f"Renovation: {self.repair}")
        pdf_canvas.drawString(100, 720, f"Equipment: {self.equipment}")
        pdf_canvas.drawString(100, 700, f"Products: {self.products}")
        pdf_canvas.drawString(100, 680, f"Documentation: {self.documents}")
        pdf_canvas.drawString(100, 660, f"Salary: {self.fot}")
        pdf_canvas.drawString(100, 640, f"Sequrity: {self.guard}")
        pdf_canvas.drawString(100, 620, f"Social Media Marketing: {self.smm}")
        pdf_canvas.drawString(100, 600, f"Service: {self.service}")
        pdf_canvas.drawString(100, 580, f"Taxes: {self.tax}")

        pdf_canvas.drawString(100, 540, f"Visitor and average check: {self.tax}")

        pdf_canvas.drawString(100, 520, f"Average check: {self.num_av_check}")
        pdf_canvas.drawString(100, 500, f"Average visitors: {self.average}")

        pdf_canvas.drawString(100, 460, f"Monthly expenses:")

        pdf_canvas.drawString(100, 440, f"Average monthly expenses: {self.expenses}")

        self.final_frame = FinalBlock(self.root,
                              self.result,
                              self.ivest,
                              self.result_list,
                              self.expenses)
        
        
        pdf_canvas.drawString(100, 400, f"Client data: {self.final_frame.for_blocks[0][1]}, {self.final_frame.for_blocks[0][2]}, {self.final_frame.for_blocks[0][3]}, {self.final_frame.for_blocks[0][4]}")
        pdf_canvas.drawString(100, 380, f"Contract number: {self.final_frame.contract_id}")
        pdf_canvas.drawString(100, 360, f"Manager ID: {self.final_frame.cd[0][2]}")







    # Закрываем PDF-документ
        pdf_canvas.save()
    def payback_task(self):
        
        initial_rent = int(self.entry_initial_rent.get())
        repair = int(self.entry_repair.get())
        equipment = int(self.entry_equipment.get())
        products = int(self.entry_products.get())
        documents = int(self.entry_documents.get())
        fot = int(self.entry_fot.get())
        guard = int(self.entry_guard.get())
        smm = int(self.entry_smm.get())
        service = int(self.entry_service.get())
        tax = int(self.entry_tax.get())

        self.ivest = initial_rent + repair + equipment + products + documents + fot + guard + smm + service + tax

        #print("invest ", ivest)

        ######
    
        entry_v1 = self.entry_visitors1.get()
        entry_v2 = self.entry_visitors2.get()
        entry_v3 = self.entry_visitors3.get()
        entry_v4 = self.entry_visitors4.get()
        entry_v5 = self.entry_visitors5.get()
        av_check = int(self.entry_average_check.get())
        input_numbers = [entry_v1, entry_v2, entry_v3, entry_v4, entry_v5]
        generator = VisitorsGenerator()
        num_av_check = int(av_check)
        visitors_list = generator.generate_visitors(input_numbers)
        self.result_list = [int(x) * num_av_check for x in visitors_list]

        ######

        entry_month_rent = self.entry_month_rent.get()
        entry_month_repair = self.entry_month_repair.get()
        entry_month_products = self.entry_month_products.get()
        entry_month_fot = self.entry_month_fot.get()
        entry_month_guard = self.entry_month_guard.get()
        entry_month_smm = self.entry_month_smm.get()
        entry_month_service= self.entry_month_service.get()
        self.expenses = int(entry_month_rent) + int(entry_month_guard) + int(entry_month_products) + int(entry_month_repair) + int(entry_month_fot) + int(entry_month_service) + int(entry_month_smm)
        
        self.income_frame.destroy()
        self.investment_frame.destroy()
        self.expenses_frame.destroy()

        self.final_frame = FinalBlock(self.root,
                                      self.result,
                                      self.ivest,
                                      self.result_list,
                                      self.expenses)
        self.final_frame.display_block()

        self.payback = PaybackCalculator(
            int(self.ivest),
            self.result_list,
            int(self.expenses)
        )
        self.payback.plot_payback_graph()
        self.payback.plot_profit_graph()
        self.months = self.payback.calculate_payback_time()

#####
#####
#####
#####
#####
#####
        
    def write_invested_to_database(self):
        # Получаем значения из полей ввода
        contract = self.result
        initial_rent = self.entry_initial_rent.get()
        repair = self.entry_repair.get()
        equipment = self.entry_equipment.get()
        products = self.entry_products.get()
        documents = self.entry_documents.get()
        fot = self.entry_fot.get()
        guard = self.entry_guard.get()
        smm = self.entry_smm.get()
        service = self.entry_service.get()
        tax = self.entry_tax.get()

        ######
        
        entry_v1 = self.entry_visitors1.get()
        entry_v2 = self.entry_visitors2.get()
        entry_v3 = self.entry_visitors3.get()
        entry_v4 = self.entry_visitors4.get()
        entry_v5 = self.entry_visitors5.get()
        av_check = self.entry_average_check.get()

        ######

        entry_month_rent = self.entry_month_rent.get()
        entry_month_repair = self.entry_month_repair.get()
        entry_month_products = self.entry_month_products.get()
        entry_month_fot = self.entry_month_fot.get()
        entry_month_guard = self.entry_month_guard.get()
        entry_month_smm = self.entry_month_smm.get()
        entry_month_service= self.entry_month_service.get()

        # Подключение к базе данных PostgreSQL
        connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="123"
        )
        cursor = connection.cursor()

        query = "INSERT INTO invested (contract_id, rent, repair, equipment, products, documents, salary, security, publicity, utility_costs, taxes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (contract, initial_rent, repair, equipment, products, documents, fot, guard, smm, service, tax))
        connection.commit()

        ###

        query = "INSERT INTO income (contract_id, month, visitor_count, avg_check) VALUES (%s, %s, %s, %s);"
        cursor.execute(query, (contract, 1, entry_v1, av_check))
        connection.commit()
        query = "INSERT INTO income (contract_id, month, visitor_count, avg_check) VALUES (%s, %s, %s, %s);"
        cursor.execute(query, (contract, 2, entry_v2, av_check))
        connection.commit()
        query = "INSERT INTO income (contract_id, month, visitor_count, avg_check) VALUES (%s, %s, %s, %s);"
        cursor.execute(query, (contract, 3, entry_v3, av_check))
        connection.commit()
        query = "INSERT INTO income (contract_id, month, visitor_count, avg_check) VALUES (%s, %s, %s, %s);"
        cursor.execute(query, (contract, 4, entry_v4, av_check))
        connection.commit()
        query = "INSERT INTO income (contract_id, month, visitor_count, avg_check) VALUES (%s, %s, %s, %s);"
        cursor.execute(query, (contract, 5, entry_v5, av_check))
        connection.commit()

        ###

        query = "INSERT INTO expenses (contract_id, rent, repair, products, salary, security, publicity, utility_costs) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (contract ,entry_month_rent, entry_month_repair, entry_month_products, entry_month_fot, entry_month_guard, entry_month_smm, entry_month_service))
        connection.commit()        

        # Закрытие соединения
        connection.close()        


if __name__ == "__main__":
    root = tk.Tk()
    app = Blocks(root, 3)
    root.mainloop()
