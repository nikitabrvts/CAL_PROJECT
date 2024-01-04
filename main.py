# main.py

import tkinter as tk
from tkinter import ttk
from auth_form import AuthForm
from matplotlib.backends.backend_pdf import PdfPages


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Главное окно")

        pdf = PdfPages("results.pdf")

        # Создаем экземпляр класса AuthForm для формы авторизации
        self.auth_form = AuthForm(self.root)
        # Подключаем метод обработки успешной авторизации
#        self.auth_form.set_login_success_callback(self.show_blocks)

#    def show_blocks(self):
        # Создаем экземпляр класса Blocks только после успешной авторизации
#        self.blocks = Blocks(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
