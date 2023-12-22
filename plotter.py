# plotter.py

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Plotter:
    def __init__(self, parent_frame, monthly_data):
        self.parent_frame = parent_frame
        self.monthly_data = monthly_data

    def plot_profitability_chart(self):
        # Создаем фигуру для графика
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)

        # Данные для графика
        months = [f"Месяц {i+1}" for i in range(len(self.monthly_data))]
        profits = self.monthly_data

        # Строим график рентабельности по месяцам
        ax.plot(months, profits, marker='o', label='Рентабельность')

        # Добавляем заголовок и метки
        ax.set_title('График рентабельности по месяцам')
        ax.set_xlabel('Месяц')
        ax.set_ylabel('Рентабельность')

        # Добавляем легенду
        ax.legend()

        # Создаем объект для встраивания графика в Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.parent_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=2, column=0, pady=10)