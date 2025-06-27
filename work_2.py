from typing import Callable
import re

# Створюємо генератор
def generator_numbers(text: str):
    pattern = r"\d+\.?\d+"
    incomes = re.findall(pattern, text)
    for income in incomes:
        yield float(income)

# Створюємо функцію sum_profit для підсумовуння доходів
def sum_profit(text: str, func: Callable):
    return sum([_ for _ in func(text)])

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)

# Альтернативний варіант без функцій :)
# total_income = sum([float(_) for _ in re.findall(r"\d+\.?\d+", text)])

print(f"Загальний дохід: {total_income}")