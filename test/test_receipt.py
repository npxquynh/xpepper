import unittest
from receipt import Receipt

class TestReceiptMethods(unittest.TestCase):
    def setUp(self):
        self.receipt = Receipt()

    def test_round(self):
        self.assertAlmostEqual(self.receipt._round(3.81, 0.05), 3.85)
        self.assertAlmostEqual(self.receipt._round(3.85, 0.05), 3.85)
        self.assertAlmostEqual(self.receipt._round(3.86, 0.05), 3.90)
        self.assertAlmostEqual(self.receipt._round(3.9, 0.05), 3.90)

    def test_imported_food(self):
        self.receipt.add(1, "imported box of chocolates", 11.25)
        self.assertAlmostEqual(self.receipt.tax[0], 0.05)
        self.assertAlmostEqual(self.receipt.calculate_final_price(0), 11.85)

    def test_local_food(self):
        self.receipt.add(1, "chocolate bar", 0.85)
        self.assertAlmostEqual(self.receipt.tax[0], 0.0)
        self.assertAlmostEqual(self.receipt.calculate_final_price(0), 0.85)

    def test_imported_general_product(self):
        self.receipt.add(1, "imported bottle of perfume", 47.5)
        self.assertAlmostEqual(self.receipt.tax[0], 0.15)
        self.assertAlmostEqual(self.receipt.calculate_final_price(0), 54.65)

    def test_general_product(self):
        self.receipt.add(1, "music CD", 14.99)
        self.assertAlmostEqual(self.receipt.tax[0], 0.10)
        self.assertAlmostEqual(self.receipt.calculate_final_price(0), 16.49)

if __name__ == '__main__':
    unittest.main()