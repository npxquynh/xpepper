import unittest
from good_category import GoodCategory

class TestGoodCategory(unittest.TestCase):
    def setUp(self):
        self.category = GoodCategory()

    def test_classify(self):
        description = [
            "imported box of chocolates",
            "chocolate bar",
            "packet of headache pills",
            "book",
            "imported bottle of perfume",
            "music CD",
        ]
        category = [
            "food",
            "food",
            "med",
            "book",
            "other",
            "other",
        ]
        for i in range(len(description)):
            self.assertEqual(category[i], self.category.classify(description[i]))

if __name__ == '__main__':
    unittest.main()