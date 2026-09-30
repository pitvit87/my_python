print("Task 5: ")
import math


def count_log_iterations(x: float) -> int:
    """
    Рахує, скільки разів потрібно взяти натуральний логарифм числа x,
    щоб отримати значення менше 1.
    """
    if x <= 0:
        raise ValueError("Число повинно бути більшим за 0, оскільки ln(x) визначений лише для x > 0.")

    iterations = 0
    while x >= 1:
        x = math.log(x)
        iterations += 1

    return iterations


# Приклади використання:
print(f"Для 0.5: {count_log_iterations(0.5)} ітерацій")  # Вже менше 1
print(f"Для e (2.718): {count_log_iterations(math.e)} ітерацій")  # ln(e) = 1, ln(1) = 0 (менше 1) -> 2 ітерації
print(f"Для 10: {count_log_iterations(10)} ітерацій")
print(f"Для 1000: {count_log_iterations(1000)} ітерацій")