import tkinter as tk
from tkinter import ttk

import psycopg2

from time_to_payback import PaybackCalculator
from visitors_generator import VisitorsGenerator

class FinalBlock:
    def __init__(self, root, contract_id, initial_budget, total_income, monthly_expenses):


        # Инициализация подключения к базе данных PostgreSQL
        self.connection = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="123"
        )
        self.cursor = self.connection.cursor()    
        self.contract_id = contract_id
        self.initial_budget = initial_budget*1.15
        self.total_income = total_income
        self.monthly_expenses = monthly_expenses
        contract_data = self.fetch_contract_data(contract_id)
        self.cd =contract_data
        client_data = self.fetch_client_data([(contract_data[0][1])])
        self.for_blocks = client_data
        self.manager_id = 0
        invest_data = self.fetch_invested_data(contract_id)
        income_data = self.fetch_income_data(contract_id)
        expens_data = self.fetch_expens_data(contract_id)
        payback_data  = PaybackCalculator(self.initial_budget, self.total_income, self.monthly_expenses)
        payback_month = payback_data.calculate_payback_time()
        self.av = self.fetch_income_data_av(contract_id)
       
        self.final_frame = ttk.Frame(root, borderwidth=2, relief="solid", width=400, height=200)

        ttk.Label(self.final_frame, text="Итоговые результаты", style="TLabel").grid(row=0, column=0, pady=5)

        ttk.Label(self.final_frame, text="Данные клиента:").grid(row=1, column=0, pady=5, sticky="w", padx=5)
        self.client_data_label = ttk.Label(self.final_frame, text=client_data[0][1] + " " 
                                           + client_data[0][2] + " " 
                                           + client_data[0][3] + " " + "\n" 
                                           + client_data[0][4] + " " + "\n"
                                           + client_data[0][5]  )
        self.client_data_label.grid(row=1, column=1, pady=5, sticky="w", padx=5)

        ttk.Label(self.final_frame, text="Номер договора:").grid(row=2, column=0, pady=5, sticky="w", padx=5)
        self.contract_number_label = ttk.Label(self.final_frame, text=contract_id)
        self.contract_number_label.grid(row=2, column=1, pady=5, sticky="w", padx=5)

        ttk.Label(self.final_frame, text="Идентификатор менеджера:").grid(row=3, column=0, pady=5, sticky="w", padx=5)
        self.manager_id_label = ttk.Label(self.final_frame, text=contract_data[0][2])
        self.manager_id_label.grid(row=3, column=1, pady=5, sticky="w", padx=5)

        ttk.Label(self.final_frame, text="Расходы до открытия: ").grid(row=4, column=0, pady=5, sticky="w", padx=5)

        self.input_params_label = ttk.Label(self.final_frame, text=" Аренда: " + str(invest_data[0][1]) + "\n" +
                                                            " Ремонт: " + str(invest_data[0][2]) + "\n" +
                                                            " Оборудование: " + str(invest_data[0][3]) + "\n" +
                                                            " Продукты: " + str(invest_data[0][4]) + "\n" +
                                                            " Документы: " + str(invest_data[0][5]) + "\n" +
                                                            " ФОТ: " + str(invest_data[0][6]) + "\n" +
                                                            " Охрана: " + str(invest_data[0][7]) + "\n" +
                                                            " Маркетинг: " + str(invest_data[0][8]) + "\n" +
                                                            " Коммунальные платежи: " + str(invest_data[0][9]) + "\n" +
                                                            " Налоги: " + str(invest_data[0][10]) + "\n").grid(row=4, column=1, pady=5, sticky="w", padx=5)


        ttk.Label(self.final_frame, text="Гости и средний чек:").grid(row=5, column=0, pady=5, sticky="w", padx=5)

        self.input_params_label = ttk.Label(self.final_frame, text=
                                                            "Среднее предполагаемое количество гостей: " + str(income_data[4][2]) + "\n" +
                                                            "Средний чек: " + str((income_data[0][3]))
                                                            ).grid(row=5, column=1, pady=5, sticky="w", padx=5)
        
        ttk.Label(self.final_frame, text="Ежемесячные расходы:").grid(row=6, column=0, pady=5, sticky="w", padx=5)

        self.input_params_label = ttk.Label(self.final_frame, text="Аренда: " + str(expens_data[0][2]) + "\n" +
                                                            " Ремонт: " + str(expens_data[0][3]) + "\n" +
                                                            " Продукты: " + str(expens_data[0][4]) + "\n" +
                                                            " ФОТ: " + str(expens_data[0][5]) + "\n" +
                                                            " Охрана: " + str(expens_data[0][6]) + "\n" +
                                                            " Маркетинг: " + str(expens_data[0][7]) + "\n" +
                                                            " Коммунальные платежи: " + str(expens_data[0][8])
                                                            ).grid(row=6, column=1, pady=5, sticky="w", padx=5)



        ttk.Label(self.final_frame, text="Результаты расчета:").grid(row=7, column=0, pady=5, sticky="w", padx=5)
        self.calculation_results_label = ttk.Label(self.final_frame, text="Первоначальные инвестиции: " + str(int(initial_budget*1.15)) + "\n" +
                                                                          "Срок окупаемости: " + str(payback_month - 2) 
                                                                                                            )
        self.calculation_results_label.grid(row=7, column=1, pady=5, sticky="w", padx=5)

    def display_block(self):
        # Метод для отображения блока
        self.final_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    def fetch_contract_data(self, contract_id):
        query = "SELECT * FROM contract WHERE contract_id = %s;"
        self.cursor.execute(query, (contract_id,))
        contract_data = self.cursor.fetchall()
        return contract_data
    
    def fetch_client_data(self, client_id):
        query = "SELECT * FROM client WHERE client_id = %s;"
        self.cursor.execute(query, (client_id))
        client_data = self.cursor.fetchall()
        return client_data
    
    def fetch_invested_data(self, contract_id):
        query = "SELECT * FROM invested WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        invest_data = self.cursor.fetchall()
        return invest_data
    
    def fetch_income_data(self, contract_id):
        query = "SELECT * FROM income WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        income_data = self.cursor.fetchall()
        return income_data
    
    def fetch_expens_data(self, contract_id):
        query = "SELECT * FROM expenses WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        expens_data = self.cursor.fetchall()
        return expens_data
    
    def fetch_income_data_av(self, contract_id):
        query = "SELECT * FROM income WHERE contract_id = %s;"
        self.cursor.execute(query, ([contract_id]))
        income_data = self.cursor.fetchall()
        input_numbers = [income_data[0][2], income_data[1][2], income_data[2][2], income_data[3][2], income_data[4][2]]
        generator = VisitorsGenerator()
        visitors_list = generator.generate_visitors(input_numbers)
        sum_of_list = 0
        for i in range(len(visitors_list)):
            sum_of_list += int(visitors_list[i])
        average = int(sum_of_list/len(visitors_list))
        return average



    def close_connection(self):
        # Закрытие соединения с базой данных
        self.connection.close()




# Пример использования
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Test Application")

    # Создаем объект класса FinalBlock
    final_block = FinalBlock(root, 3, 100,[0, 500, 300, 300, 9000, 300],20)

    # Вызываем метод для отображения блока
    final_block.display_block()

    #final_block.fetch_contract_data(10)

    # Запускаем цикл обработки событий
    root.mainloop()
