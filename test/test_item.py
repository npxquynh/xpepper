import unittest
import mock
from mock import Mock
from mock import patch
from item import Item
from good_category import GoodCategory

class ItemTestCase(unittest.TestCase):
    def setUp(self):
        self.imported_description = 'imported product description'
        self.description = "product description"

    @patch.object(Item, 'calculate_tax_imported', return_value=0.1)
    @patch.object(Item, 'calculate_basic_sales_tax', return_value=0.2)
    def test_calculate_tax(self, patch_tax_imported, patch_basic_sales_tax):
        result = Item.calculate_tax(self.imported_description)
        self.assertEqual(result, 0.1)
        Item.calculate_tax_imported.assert_called_once_with(self.imported_description)

        result = Item.calculate_tax(self.description)
        self.assertEqual(result, 0.2)
        Item.calculate_basic_sales_tax.assert_called_once_with(self.description)

    @patch.object(Item, 'calculate_basic_sales_tax', return_value=0.0)
    def test_calculate_tax_imported(self, patch_basic_sales_tax):
        result = Item.calculate_tax_imported(self.description)
        Item.calculate_basic_sales_tax.assert_called_once_with(self.description)
        self.assertEqual(result, 0.05)

    @patch.object(Item, 'is_tax_exempted')
    def test_calculate_basic_sales_tax(self, mock_tax_exempted):
        mock_tax_exempted.return_value = False
        result = Item.calculate_basic_sales_tax(self.description)
        Item.is_tax_exempted.assert_called_with(self.description)
        self.assertEqual(result, Item.BASIC_TAX)

        mock_tax_exempted.return_value = True
        result = Item.calculate_basic_sales_tax(self.description)
        Item.is_tax_exempted.assert_called_with(self.description)
        self.assertEqual(result, 0)

    @patch.object(GoodCategory, 'classify')
    def test_is_tax_exempted(self, classifier):
        for type in ["book", "med", "food"]:
            classifier.return_value = type
            result = Item.is_tax_exempted(self.description)
            classifier.assert_called_with(self.description)
            self.assertEqual(result, True)

        classifier.return_value = ""
        result = Item.is_tax_exempted(self.description)
        classifier.assert_called_with(self.description)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()