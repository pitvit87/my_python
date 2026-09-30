print("Task 4")

import math

def arc_length(radius, angle):
    angle = math.radians(angle)
    return radius * angle


r = float(input("Введите радиус: "))
a = float(input("Введите угол в градусах: "))

print("Длина дуги:", arc_length(r, a))