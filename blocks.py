import tkinter as tk
from tkinter import ttk
import psycopg2
from calculator import Calculator
from pdf_exporter import PDFExporter
from plotter import Plotter
from time_to_payback import PaybackCalculator
from visitors_generator import VisitorsGenerator

class Blocks:
    def __init__(self, root, result):

        self.root = root
        self.result = result

        self.root.title("Блоки с данными")

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
        self.calculator = Calculator(self)
        self.calculate_button = ttk.Button(root, text="из полей в 3 таблицы", command=self.write_invested_to_database)
        self.calculate_button.grid(row=0, column=4, pady=10)

        # Кнопка "Рассчитать"
        self.calculator = Calculator(self)
        self.calculate_button = ttk.Button(root, text="вызов калькулятора", command=self.payback_task)
        self.calculate_button.grid(row=1, column=4, pady=10)

        # Кнопка "Рассчитать"
        self.calculator = Calculator(self)
        self.calculate_button = ttk.Button(root, text="Рассчитать", command=self.write_invested_to_database)
        self.calculate_button.grid(row=2, column=4, pady=10)

        # Опция для минимальной высоты строки
        root.grid_rowconfigure(3, weight=1)

        # Создаем экземпляр класса Calculator, передавая текущий экземпляр Blocks
        self.calculator = Calculator(self)

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

        ivest = initial_rent + repair + equipment + products + documents + fot + guard + smm + service + tax

        print("invest ", ivest)

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

        result_list = [int(x) * num_av_check for x in visitors_list]
        print("выручка по месяцам:", result_list)

        ######

        entry_month_rent = self.entry_month_rent.get()
        entry_month_repair = self.entry_month_repair.get()
        entry_month_products = self.entry_month_products.get()
        entry_month_fot = self.entry_month_fot.get()
        entry_month_guard = self.entry_month_guard.get()
        entry_month_smm = self.entry_month_smm.get()
        entry_month_service= self.entry_month_service.get()

        expenses = int(entry_month_rent) + int(entry_month_guard) + int(entry_month_products) + int(entry_month_repair) + int(entry_month_fot) + int(entry_month_service) + int(entry_month_smm)

        print("expenses " ,expenses)
        
        self.payback = PaybackCalculator(
            int(ivest),
            result_list,
            int(expenses)
        )


    #####

    def calculate(self):
        print(self.start_invest)
        # Вызываем метод calculate из экземпляра класса Calculator
        # self.calculator.calculate()

    def show_results(self, total_income, total_expenses):
        # Создаем новый блок с результатами
        result_frame = ttk.Frame(self.root, style="TFrame")
        result_frame.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        # Создаем экземпляр класса PDFExporter
        self.pdf_exporter = PDFExporter("results.pdf")

        # Добавляем кнопку "Экспорт в PDF"
        ttk.Button(self.root, text="Экспорт в PDF", command=lambda: self.pdf_exporter.export_to_pdf(total_income, total_expenses)).grid(row=2, column=3, pady=10)

        # Выводим результаты в новый блок
        ttk.Label(result_frame, text=f"Общий доход: {total_income}").grid(row=0, column=0, pady=5)
        ttk.Label(result_frame, text=f"Общие расходы: {total_expenses}").grid(row=1, column=0, pady=5)

        # Переменные для хранения данных
        self.total_income = tk.StringVar()
        self.total_expenses = tk.StringVar()

        # Опция для минимальной высоты строки
        self.root.grid_rowconfigure(4, weight=1)

        # Добавляем график рентабельности по месяцам
        monthly_data = [total_income, 12000, 8000, 15000]  # Пример данных по месяцам
        plotter = Plotter(result_frame, monthly_data)
        plotter.plot_profitability_chart()

        # Скрываем кнопку "Рассчитать"
        self.calculate_button.grid_forget()
        # Очищаем старые блоки
        self.investment_frame.destroy()
        self.income_frame.destroy()
        self.expenses_frame.destroy()

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
