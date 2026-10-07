import math

def get_valid_float(prompt: str) -> float:
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Помилка! Будь ласка, введіть коректне число (наприклад: 60, 45.5 або -90).\n")


def calculate_cosine(degrees: float) -> float:
    radians = math.radians(degrees)
    return math.cos(radians)


def main():
    angle = get_valid_float("Введіть кут у градусах: ")
    cos_value = calculate_cosine(angle)

    print(f"cos({angle}°) = {round(cos_value, 4)}")


main()
