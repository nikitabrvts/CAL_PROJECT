
from final_block import FinalBlock


class PaybackCalculator:
        
        # Создание объекта FinalBlock
        final_block = FinalBlock()
        final_block.final_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")


        # После выполнения вычислений, обновление результатов в блоке
        final_block.update_client_data("Иванов Иван Иванович, телефон: 123-456")
        final_block.update_contract_number("12345")
        final_block.update_manager_id("567")
        final_block.update_input_params("Аренда: $1000, Ремонт: $500, ...")
        final_block.update_calculation_results("Первоначальные инвестиции: $2000, Срок окупаемости: 6 месяцев, Рентабельность: 15%")
