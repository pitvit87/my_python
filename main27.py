
print("\n-------------------------------------------------- Task 1 -------------------------------------------------\n")

class Car:
    def __init__(self, model, year, producer, engine, color,  price):
        self.model = model
        self.year = year
        self.producer = producer
        self.engine = engine
        self.color = color
        self.price = price


    def __str__(self):
        return  f"{self.producer} {self.model}, {self.year} року випуску, з об'ємом двигуна {self.engine}" \
              f", колір якої {self.color}, за ціною - {self.price}$\n"


    def sold_discount(self):
        print(f"{self.producer} {self.model}, {self.year} року випуску - була продана зі знижкою 5% за "
              f"{self.price * 0.95}$!\n")


car1 = Car("Accord", 2015, "Honda", 2.4, "Синій", 8000)
print(car1)
car1.sold_discount()


print("-------------------------------------------------- Task 2 -------------------------------------------------\n")

class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price


    def show_details(self):
        print(f"\"{self.name}\", {self.year} року випуску, від видавця \"{self.publisher}\", у жанрі - {self.genre},"
              f"від автора {self.author}, за ціною {self.price} грн.\n")


    def __str__(self) -> str:
        return f"\"{self.name}\" {self.year} від {self.author} за {self.price} грн."


book1 = Book("Кобзар", 1976, "Днипро", "Поезія", "Т.Г. Шевченко", 12500)
print(book1)
print(f"\nРозгорнута інформація: ")
book1.show_details()


print("-------------------------------------------------- Task 3 --------------------------------------------------\n")

class Stadium:
    def __init__(self, name, opening, country, city, places):
        self.name = name
        self.opening = opening
        self.country = country
        self.city = city
        self.places = places


    def __str__(self):
        return f"\"{self.name}\". Був відкритий {self.opening} в місті - {self.city}, {self.country}. " \
               f"Розрахований на {self.places} глядачів.\n"


    def wellcome(self):
        print(f"Ви можете придбати квитки на фінал України по футболу, що відбудеться на наступні вихідні в м. "
              f"{self.city} ({self.country}),\nмісце проведення - \"{self.name}\". Місткість стадіону {self.places}"
              f" місць.")


stadium1 = Stadium("Олімпійський стадіон", "12.08.1996", "Україна", "Київ", 70500)
print(stadium1)
stadium1.wellcome()