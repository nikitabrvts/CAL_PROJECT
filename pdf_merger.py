import PyPDF2

class PDFMerger:
    def __init__(self, output_filename):
        self.output_filename = output_filename
        self.pdf_merger = PyPDF2.PdfMerger()

    def add_pdf(self, pdf_filename):
        with open(pdf_filename, 'rb') as pdf_file:
            self.pdf_merger.append(pdf_file)

    def merge_pdfs(self):
        with open(self.output_filename, 'wb') as output_file:
            self.pdf_merger.write(output_file)

# Пример использования
#pdf_merger = PDFMerger("RESULT.pdf")
#pdf_merger.add_pdf("1.pdf")
#pdf_merger.add_pdf("payback_graph.pdf")
#pdf_merger.add_pdf("profit_graph.pdf")
#pdf_merger.merge_pdfs()
