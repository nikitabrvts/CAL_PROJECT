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
        self.investment_frame = ttk.Frame(root, style="TFrame")
        self.investment_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.investment_frame, text="Первоначальные инвестиции", style="TLabel").grid(row=0, column=0, pady=5)

        ttk.Label(self.investment_frame, text="Первоначальная аренда:", style="TLabel").grid(row=1, column=0, pady=5)
        self.entry_initial_rent = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_initial_rent.grid(row=1, column=1, pady=5)

        ttk.Label(self.investment_frame, text="Ремонт:", style="TLabel").grid(row=2, column=0, pady=5)
        self.entry_repair = ttk.Entry(self.investment_frame, style="TEntry")
        self.entry_repair.grid(row=2, column=1, pady=5)

        # Добавьте другие поля для "Первоначальные инвестиции" по аналогии

        # Опция для минимальной высоты строки
        self.investment_frame.grid_rowconfigure(0, weight=1)
        self.investment_frame.grid_rowconfigure(1, weight=1)
        self.investment_frame.grid_rowconfigure(2, weight=1)

        # Блок "Доходы"
        self.income_frame = ttk.Frame(root, style="TFrame")
        self.income_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.income_frame, text="Доходы", style="TLabel").grid(row=0, column=0, pady=5)

        ttk.Label(self.income_frame, text="Количество посетителей:", style="TLabel").grid(row=1, column=0, pady=5)
        self.entry_visitors = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_visitors.grid(row=1, column=1, pady=5)

        ttk.Label(self.income_frame, text="Средний чек:", style="TLabel").grid(row=2, column=0, pady=5)
        self.entry_average_check = ttk.Entry(self.income_frame, style="TEntry")
        self.entry_average_check.grid(row=2, column=1, pady=5)

        # Добавьте другие поля для "Доходы" по аналогии

        # Опция для минимальной высоты строки
        self.income_frame.grid_rowconfigure(0, weight=1)
        self.income_frame.grid_rowconfigure(1, weight=1)
        self.income_frame.grid_rowconfigure(2, weight=1)

        # Блок "Расходы"
        self.expenses_frame = ttk.Frame(root, style="TFrame")
        self.expenses_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(self.expenses_frame, text="Расходы", style="TLabel").grid(row=0, column=0, pady=5)

        ttk.Label(self.expenses_frame, text="Аренда:", style="TLabel").grid(row=1, column=0, pady=5)
        self.entry_rent = ttk.Entry(self.expenses_frame, style="TEntry")
        self.entry_rent.grid(row=1, column=1, pady=5)

        ttk.Label(self.expenses_frame, text="Продукты:", style="TLabel").grid(row=2, column=0, pady=5)
        self.entry_products_expenses = ttk.Entry(self.expenses_frame, style="TEntry")
        self.entry_products_expenses.grid(row=2, column=1, pady=5)

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
        self.calculate_button.grid(row=3, column=0, pady=10)

        # Опция для минимальной высоты строки
        root.grid_rowconfigure(3, weight=1)

        # Создаем экземпляр класса Calculator, передавая текущий экземпляр Blocks
        self.calculator = Calculator(self)

    def calculate(self):
        # Вызываем метод calculate из экземпляра класса Calculator
        self.calculator.calculate()

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
