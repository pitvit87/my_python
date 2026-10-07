from datetime import date


def get_valid_date(prompt: str) -> date:
    while True:
        user_input = input(prompt).strip()
        try:
            return date.fromisoformat(user_input)
        except ValueError:
            print("Помилка! Перевірте формат або реальність дати.")
            print("Переконайтеся, що формат YYYY-MM-DD (наприклад, 2026-10-07) і така дата існує.\n")


def days_between_dates():
    date1 = get_valid_date("Введіть початкову дату (YYYY-MM-DD): ")
    date2 = get_valid_date("Введіть кінцеву дату (YYYY-MM-DD): ")

    delta_days = abs((date2 - date1).days)

    print(f"Кількість днів між {date1} та {date2} становить: {delta_days} днів.")


days_between_dates()


