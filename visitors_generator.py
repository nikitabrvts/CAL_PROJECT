import random

class VisitorsGenerator:
    @staticmethod
    def generate_visitors(numbers):
        # Первые 5 чисел
        initial_numbers = numbers[:5]
        
        # Генерация оставшихся 15 случайных чисел в пределах 30% от 5го числа
        random_numbers = [round(random.uniform(0.7 * initial_numbers[4], 1.3 * initial_numbers[4])) for _ in range(21)]
        
        # Объединение списков
        result = initial_numbers + random_numbers
        
        return result

# Пример использования:
if __name__ == "__main__":
    input_numbers = [100, 150, 200, 250, 300]
    generator = VisitorsGenerator()
    visitors_list = generator.generate_visitors(input_numbers)
    print("Список посетителей:", visitors_list)
