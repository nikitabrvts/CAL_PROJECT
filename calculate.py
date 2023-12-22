

from pdf_exporter import PDFExporter


class Calculator:
    def __init__(self, blocks_instance):
        self.blocks_instance = blocks_instance

    def calculate(self):
        # Получаем значения из полей ввода
        # Получаем значения из полей ввода
        visitors = float(self.blocks_instance.entry_visitors.get())
        average_check = float(self.blocks_instance.entry_average_check.get())
        rent = float(self.blocks_instance.entry_rent.get())
        products_expenses = float(self.blocks_instance.entry_products_expenses.get())
        # Добавьте другие необходимые поля ввода

        # Пример простых вычислений
        total_income = visitors * average_check
        total_expenses = rent + products_expenses  # Добавьте другие расходы по аналогии

        # Вызываем метод blocks_instance.show_results, передавая результаты расчетов
        self.blocks_instance.show_results(total_income, total_expenses)

        # Создаем экземпляр класса PDFExporter и экспортируем результаты в PDF
        pdf_exporter = PDFExporter("results.pdf")
        pdf_exporter.export_to_pdf(self, total_income, total_expenses)