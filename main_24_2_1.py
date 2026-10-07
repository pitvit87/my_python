import math

x = float(input("Введіть число для пошуку кількості ітерацій його логарифма: "))

def count_log_iterations(x: float) -> int:
    if x <= 0:
        raise ValueError("Число має бути більшим за 0, оскільки логарифм від'ємних чисел та нуля не існує.")

    count = 0
    while x >= 1:
        x = math.log(x)
        count += 1
    return count

print(f"Для числа {x} кількості ітерацій його логарифма: {count_log_iterations(x)}")