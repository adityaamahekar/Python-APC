#multilevel inheritance

#A -> B -> C

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Quantity(Book):
    def __init__(self, title, author, quantity):
        super().__init__(title, author)
        self.quantity = quantity

    def display_quantity(self):
        self.display_info()
        print(f"Quantity: {self.quantity}")

class Price(Quantity):
    def __init__(self, title, author, quantity, price):
        super().__init__(title, author, quantity)
        self.price = price

    def display_price(self):
        self.display_quantity()
        print(f"Price: {self.price}")

print("----|| Book Details ||----")
print("--------------------------------------")

p=Price("The Great Gatsby", "F. Scott Fitzgerald", 3, 1599)
p.display_price()

print("--------------------------------------")

p1=Price("To Kill a Mockingbird", "Harper Lee", 5, 1299)
p1.display_price()