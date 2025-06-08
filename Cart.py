# cart.py

from product import Product

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product: Product, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        self.items.append((product, quantity))

    def total(self):
        return sum(p.price * q for p, q in self.items)

    def clear(self):
        self.items = []
