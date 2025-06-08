# product.py

class Product:
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.name = name
        self.price = price
