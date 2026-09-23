import math

print("1 задача! ")
print("Знайти радіус кола: ")

def square_circuit(rad):
    square_circ = math.pi * math.pow(rad, 2)
    print(f"Площа кола з радіусом {rad} см дорівнює - {round(square_circ, 2)} см")
    return


r = float(input("Введіть радіус кола: "))

square_circuit(r)

