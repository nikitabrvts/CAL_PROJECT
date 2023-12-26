class PaybackTime:
    def __init__(self, monthly_expenses, total_income, initial_budget):
        self.monthly_expenses = monthly_expenses
        self.total_income = total_income
        self.initial_budget = initial_budget
        self.cash = self.initial_budget * -1

    def calculate_payback_time(self):
        if self.monthly_expenses <= 0:
            return "Invalid monthly expenses value. Must be greater than 0."

        if self.total_income <= 0:
            return "Invalid total income value. Must be greater than 0."

        if self.initial_budget <= 0:
            return "Invalid initial budget value. Must be greater than 0."

        # Рассчитываем количество месяцев до окупаемости
        payback_time_months = 0;
        initial_budget_hidtory = []
        while self.initial_budget>0 and payback_time_months < 36:
            self.initial_budget -= self.total_income - self.monthly_expenses
            payback_time_months +=1
            initial_budget_hidtory.append(self.initial_budget)


        print(initial_budget_hidtory)


        # payback_time_months = self.initial_budget / (self.total_income - self.monthly_expenses)

        if payback_time_months > 0:
            return f"Проект окупится за {int(payback_time_months)} месяцев."
        else:
            return "Проект не окупится."

# Пример использования
if __name__ == "__main__":
    # Создаем экземпляр класса PaybackTime
    payback_calculator = PaybackTime(monthly_expenses=200, total_income=230, initial_budget=1000)

    # Рассчитываем месяц окупаемости
    result = payback_calculator.calculate_payback_time()

    # Выводим результат
    print(result)
