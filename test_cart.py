

import unittest
from product import Product
from Cart import Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.apple = Product("Apple", 0.5)
        self.banana = Product("Banana", 1.0)

    def test_add_product(self):
        self.cart.add(self.apple, 3)
        self.assertEqual(len(self.cart.items), 1)

    def test_total(self):
        self.cart.add(self.apple, 2)  # 2 x 0.5 = 1.0
        self.cart.add(self.banana, 1)  # 1 x 1.0 = 1.0
        self.assertEqual(self.cart.total(), 2.0)

    def test_clear_cart(self):
        self.cart.add(self.apple)
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            self.cart.add(self.apple, 0)

if __name__ == '__main__':
    unittest.main()
