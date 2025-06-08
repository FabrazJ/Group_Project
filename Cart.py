# cart.py

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product, quantity=1):
        self.items.append((product, quantity))

    def total(self):
        return sum(p.price * q for p, q in self.items)

    def clear(self):
        self.items = []

    def get_items(self):
        return self.items
