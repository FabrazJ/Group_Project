# test_product.py

import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test_create_product(self):
        p = Product("Apple", 0.5)
        self.assertEqual(p.name, "Apple")
        self.assertEqual(p.price, 0.5)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            Product("Apple", -1)

if __name__ == '__main__':
    unittest.main()
