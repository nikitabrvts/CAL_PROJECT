from reportlab.pdfgen import canvas
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np
import fitz

class PDFExporter:
    def __init__(self, filename):
        self.filename = filename

    def export_to_pdf(self, total_income, total_expenses):
        # Создаем файл PDF
        with PdfPages(self.filename) as pdf:
            # Страница 1: График
            fig, ax = plt.subplots()
            X = np.linspace(-5, 5, 100)
            ax.plot(X, np.sin(X))
            pdf.savefig(fig)
            plt.close()


        

            text_filename = "text_page.pdf"
            c = canvas.Canvas(text_filename)
            c.drawString(100, 750, f"Overall income: {total_income}")
            c.drawString(100, 730, f"Overall expenses: {total_expenses}")
            c.save()

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
