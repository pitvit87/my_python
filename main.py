import math

print("1 задача! ")
print("Знайти радіус кола: ")

P = 3.14
r = float(input("Введіть радіус кола: "))
square_circuit = math.pi * math.pow(r, 2)
print(f"Площа кола з радіусом {r} см дорівнює - {round(square_circuit, 2)} см")