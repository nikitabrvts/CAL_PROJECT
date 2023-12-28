class PaybackCalculator:
    def __init__(self, initial_budget, total_income, monthly_expenses, max_months=6):
        self.initial_budget = initial_budget
        self.total_income = total_income
        self.monthly_expenses = int(monthly_expenses)
        self.max_months = max_months
        self.payback_time_months = 0
        self.initial_budget_history = []
        self.clear_profit = []
        self.month_expens = []
        self.month_expens.append(initial_budget)

        #PaybackCalculator.plot_payback_graph(self)

    def calculate_payback_time(self):
        i = 0
        while self.initial_budget > 0 and self.payback_time_months < self.max_months:
            self.initial_budget_history.append(self.initial_budget)
            self.initial_budget -= int(self.total_income[i]) - int(self.monthly_expenses)
            self.payback_time_months += 1
            
            self.clear_profit.append(self.total_income[i])
            self.month_expens.append(self.monthly_expenses)
            i += 1
        self.month_expens.remove(self.monthly_expenses)
       
        

    def plot_payback_graph(self):
        import matplotlib.pyplot as plt

        self.calculate_payback_time()

        # Построение графика
        plt.plot(range(1, self.payback_time_months + 1), self.initial_budget_history, marker='o', label='Кредитная задолженость')
        plt.plot(range(1, self.payback_time_months + 1), self.clear_profit, marker='o', label='Валовая выручка')
        plt.plot(range(1, self.payback_time_months + 1), self.month_expens, marker='o', label='Месячные расходы')

        plt.title('График окупаемости проекта')
        plt.xlabel('Месяц')
        plt.ylabel('Значение')
        plt.legend()  # Добавление легенды
        plt.grid(True)
        plt.show()


payback_calculator = PaybackCalculator(
    initial_budget=15000,
    total_income=[5000, 6000, 7000, 8000, 9000, 10000],
    monthly_expenses=2000
)
payback_calculator.plot_payback_graph()


