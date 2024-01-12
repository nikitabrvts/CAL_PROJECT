from matplotlib import pyplot as plt


class PaybackCalculator:
    def __init__(self, initial_budget, total_income, monthly_expenses, max_months=36):
        self.initial_budget = initial_budget
        self.ib = initial_budget
        self.total_income = total_income
        self.monthly_expenses = int(monthly_expenses)
        self.max_months = max_months
        self.payback_time_months = 0
        self.initial_budget_history = []
        self.clear_profit = []
        self.month_expens = []
        self.month_expens.append(initial_budget)
        self.profitobility_month = []
        
###
        #PaybackCalculator.plot_payback_graph(self)
###
    def calculate_payback_time(self):
        i = 0
        while self.initial_budget > 0  and self.payback_time_months < self.max_months:
            self.initial_budget_history.append(self.initial_budget)
            self.initial_budget -= int(self.total_income[i]) - int(self.monthly_expenses)
            self.payback_time_months += 1
            self.clear_profit.append(self.total_income[i])
            self.month_expens.append(self.monthly_expenses)
            i += 1

###
            #print("ОКУПАЕМОСТЬ ", self.payback_time_months)
###            
        g = i + 3
        while i < g and i<36:
            self.initial_budget_history.append(self.initial_budget)
            self.initial_budget -= int(self.total_income[i]) - int(self.monthly_expenses)
            self.clear_profit.append(self.total_income[i])
            self.month_expens.append(self.monthly_expenses)
            i += 1            
        del self.month_expens[-1]
        self.payback_time_months = len(self.initial_budget_history)
        return self.payback_time_months



    
    def plot_payback_graph(self):
        import matplotlib.pyplot as plt
        self.calculate_payback_time()
        self.initial_budget_history = [-x for x in self.initial_budget_history]
        # Построение графика
        plt.plot(range(1, self.payback_time_months + 1), self.initial_budget_history, marker='o', label='Чистая прибыль')
        plt.plot(range(1, self.payback_time_months + 1), self.clear_profit, marker='o', label='Валовая выручка')
        plt.plot(range(1, self.payback_time_months + 1), self.month_expens, marker='o', label='Месячные расходы')

        plt.title(' Окупаемость проекта')
        plt.xlabel('Месяц')
        plt.ylabel('Сумма, руб.')
        plt.legend()  # Добавление легенды
        plt.grid(True)
        # Сохранение графика в PDF файл
        plt.savefig('payback_graph.pdf')

        plt.show()


    def plot_profit_graph(self):
        # Call the profitability method and store the results in a variable
        profitability_results = self.profitability()   
        # Построение графика
        plt.plot(range(1, 37), profitability_results, marker='o', label='Рентабельность')
        plt.title('Рентабельность проекта')
        plt.xlabel('Месяц')
        plt.ylabel('%')
        plt.legend()  # Добавление легенды
        plt.grid(True)
        
        # Сохранение графика в PDF файл
        plt.savefig('profit_graph.pdf')
        
        # Показать график
        plt.show()


    def profitability(self):
        
        i = 0
        print(self.ib)
        var = int(self.total_income[i])-self.ib
        while i < self.max_months:
            var = var  + int(self.total_income[i]) - int(self.monthly_expenses)
            self.profitobility_month.append(((var*100) / self.ib))
          
            i += 1
            
        return (self.profitobility_month)        



#payback_calculator = PaybackCalculator(
#    initial_budget=400,
#    total_income=[0, 500, 300, 300, 300, 300],
#    monthly_expenses=50
#)
##payback_calculator.plot_payback_graph()
#payback_calculator.plot_profit_graph()