from datetime import date


def reformat_date(date_str: str) -> str:
    parsed_date = date.fromisoformat(date_str)
    return parsed_date.strftime("%d/%m/%Y")


def main():
    print("Введіть дату у форматі YYYY-MM-DD (або '0' для виходу).")

    while True:
        user_input = input("\nВведіть дату: ").strip()

        if user_input == "0":
            break

        try:
            new_date = reformat_date(user_input)
            print(f"Результат: {new_date}")

        except ValueError:
            print("Помилка! Перевірте формат або реальність дати.")
            print("Має бути YYYY-MM-DD (наприклад, 2026-10-07). Спробуйте ще раз.")


main()
