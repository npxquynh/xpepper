import unittest
from receipt import Receipt

class TestReceiptMethods(unittest.TestCase):
    def test_round(self):
        receipt = Receipt()
        self.assertAlmostEqual(receipt._round(3.81, 0.05), 3.85)
        self.assertAlmostEqual(receipt._round(3.85, 0.05), 3.85)
        self.assertAlmostEqual(receipt._round(3.86, 0.05), 3.90)
        self.assertAlmostEqual(receipt._round(3.9, 0.05), 3.90)

if __name__ == '__main__':
    unittest.main()