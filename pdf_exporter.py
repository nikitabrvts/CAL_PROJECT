from reportlab.pdfgen import canvas
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np
import fitz
from time_to_payback import PaybackCalculator

class PDFExporter:
    def __init__(self, initial_budget, total_income, monthly_expenses, filename):
        self.filename = filename
        self.initial_budget = initial_budget
        self.total_income = total_income
        self.monthly_expenses = int(monthly_expenses)

        ###
        PDFExporter.export_to_pdf(self)
        ###


    def export_to_pdf(self):
        # Создаем файл PDF
        with PdfPages(self.filename) as pdf:
            # Страница 1: График
            self.ext_gr = PaybackCalculator(
            int(self.initial_budget),
            self.total_income,
            int(self.monthly_expenses)
            )
            self.ext_gr.plot_payback_graph
        

        def merge_pdfs(input_files, output_filename):
            pdf_writer = fitz.open()
            input_file = PdfPages("results.pdf")
            for input_file in input_files:
                pdf = PdfPages("results.pdf")
                pdf_reader = fitz.open(input_file)
                pdf_writer.insert_pdf(pdf_reader)

            pdf_writer.save(output_filename)
            pdf_writer.close()

# Пример использования
        input_files = ["results.pdf", "text_page.pdf"]
        output_file = "FINAL_RESULT.pdf"
        merge_pdfs(input_files, output_file)
