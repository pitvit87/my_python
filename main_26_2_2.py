from datetime import datetime, timedelta


def calculate_arrival(start_dt: datetime, duration_hours: float) -> datetime:
    return start_dt + timedelta(hours=duration_hours)


def main():
    print("Введіть початкові дані (або '0' у будь-якому полі для виходу).")

    while True:
        try:
            start_input = input("\nВведіть дату і час початку (YYYY-MM-DD HH:MM): ").strip()
            if start_input == "0":
                break

            start_datetime = datetime.strptime(start_input, "%Y-%m-%d %H:%M")

            duration_input = input("Введіть тривалість поїздки в годинах (наприклад, 4.5 або 12): ").strip()
            if duration_input == "0":
                break

            duration = float(duration_input)

            if duration < 0:
                print("Помилка: Тривалість поїздки не може бути від'ємною!")
                continue

            arrival_datetime = calculate_arrival(start_datetime, duration)

            print("\nМаршрут розраховано:")
            print(f"Початок:  {start_datetime.strftime('%d.%m.%Y %H:%M')}")
            print(f"Тривалість: {duration} год.")
            print(f"Прибуття: {arrival_datetime.strftime('%d.%m.%Y %H:%M')}")

        except ValueError:
            print("Помилка! Перевірте правильність введення даних.")
            print("Формат дати та часу має бути точним: YYYY-MM-DD HH:MM (наприклад, 2026-10-07 14:30),")
            print("а тривалість має бути числом.")


main()
