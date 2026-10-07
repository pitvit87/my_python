import math


def calculate_ellipse_area(semi_major: float, semi_minor: float) -> float:
    return math.pi * semi_major * semi_minor


def main():
    print("Вводьте значення напівосей (або '0' у будь-якому полі для виходу).")

    while True:
        try:
            input_a = input("\nВведіть довжину великої напівосі (а): ").strip()
            if input_a == "0":
                break
            semi_major = float(input_a)

            input_b = input("Введіть довжину малої напівосі (b): ").strip()
            if input_b == "0":
                break
            semi_minor = float(input_b)
            if semi_major <= 0 or semi_minor <= 0:
                print("Помилка: Довжина напівосі має бути більшою за 0!")
                continue

            area = calculate_ellipse_area(semi_major, semi_minor)
            print(f"✨ Площа еліпса: {round(area, 4)} кв. од.")

        except ValueError:
            print("Помилка! Будь ласка, введіть коректне число (наприклад: 5 або 3.5).")


main()
