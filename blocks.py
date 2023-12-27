import tkinter as tk
from tkinter import ttk
from calculator import Calculator
from pdf_exporter import PDFExporter
from plotter import Plotter

class Blocks:
    def __init__(self, root):

        self.root = root
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

        ttk.Label(self.investment_frame, text="Аренда:", style="TLabel").grid(row=1, column=0, pady=10,  sticky="w", padx=5)
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

        self.start_invest = (
            self.entry_tax.get() +
            (self.entry_service.get()) +
            (self.entry_smm.get()) +
            (self.entry_guard.get()) +
            (self.entry_fot.get()) +
            (self.entry_documents.get()) +
            (self.entry_products.get()) +
            (self.entry_equipment.get()) +
            (self.entry_repair.get()) +
            (self.entry_initial_rent.get())
            ) 
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
        self.entry_visitors = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_visitors.grid(row=1, column=1, pady=5)

        ttk.Label(self.income_frame, text="Количество посетителей (2 мес.):", style="TLabel").grid(row=2, column=0, pady=5)
        self.entry_visitors = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_visitors.grid(row=2, column=1, pady=5)        

        ttk.Label(self.income_frame, text="Количество посетителей (3 мес.):", style="TLabel").grid(row=3, column=0, pady=5)
        self.entry_visitors = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_visitors.grid(row=3, column=1, pady=5)

        ttk.Label(self.income_frame, text="Количество посетителей (4 мес.):", style="TLabel").grid(row=4, column=0, pady=5)
        self.entry_visitors = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_visitors.grid(row=4, column=1, pady=5)

        ttk.Label(self.income_frame, text="Количество посетителей (5 мес.):", style="TLabel").grid(row=5, column=0, pady=5)
        self.entry_visitors = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_visitors.grid(row=5, column=1, pady=5)

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


        # Добавьте другие поля для "Расходы" по аналогии

        # Опция для минимальной высоты строки
        self.expenses_frame.grid_rowconfigure(0, weight=1)
        self.expenses_frame.grid_rowconfigure(1, weight=1)
        self.expenses_frame.grid_rowconfigure(2, weight=1)

        # Опция для минимальной высоты строки
        root.grid_rowconfigure(3, weight=1)

        # Кнопка "Рассчитать"
        self.calculator = Calculator(self)
        self.calculate_button = ttk.Button(root, text="Рассчитать", command=self.calculate)
        self.calculate_button.grid(row=0, column=4, pady=10)

        # Опция для минимальной высоты строки
        root.grid_rowconfigure(3, weight=1)

        # Создаем экземпляр класса Calculator, передавая текущий экземпляр Blocks
        self.calculator = Calculator(self)

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


if __name__ == "__main__":
    root = tk.Tk()
    app = Blocks(root)
    root.mainloop()
