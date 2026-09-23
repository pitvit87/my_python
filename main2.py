import math

print("2 задача! ")



def calculate_factorial(n):
    return math.factorial(n)


number = int(input("Введіть число, факторіал якого ми будемо шукати: "))
print(f"Факторіал числа {number} дорівнює {calculate_factorial(number)}")
