class PaybackCalculator:
    def __init__(self, initial_budget, total_income, monthly_expenses, max_months=36):
        self.initial_budget = initial_budget
        self.total_income = total_income
        self.monthly_expenses = monthly_expenses
        self.max_months = max_months
        self.payback_time_months = 0
        self.initial_budget_history = []

    def calculate_payback_time(self):
        while self.initial_budget > -200 and self.payback_time_months < self.max_months:
            self.initial_budget -= self.total_income - self.monthly_expenses
            self.payback_time_months += 1
            self.initial_budget_history.append(self.initial_budget)

    def plot_payback_graph(self):
        import matplotlib.pyplot as plt

        self.calculate_payback_time()

        # Построение графика
        plt.plot(range(1, self.payback_time_months + 6), self.initial_budget_history + [None] * 5, marker='o')
        plt.title('График окупаемости проекта')
        plt.xlabel('Месяц')
        plt.ylabel('Остаток до выхода на точку окупаемости')
        plt.grid(True)
        plt.show()


# Пример использования
payback_calculator = PaybackCalculator(initial_budget=1000, total_income=500, monthly_expenses=400)
payback_calculator.plot_payback_graph()
