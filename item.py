from good_category import GoodCategory

import pdb

class Item():
    IMPORT_DUTY = 0.05
    BASIC_TAX = 0.1

    good_category = GoodCategory()

    def __init__(self):
        pass

    @staticmethod
    def calculate_tax(description):
        if description.find("imported") != -1:
            return Item.calculate_tax_imported(description)
        else:
            return Item.calculate_basic_sales_tax(description)

    @staticmethod
    def calculate_tax_imported(description):
        basic_sales_tax = Item.calculate_basic_sales_tax(description)
        return basic_sales_tax + Item.IMPORT_DUTY

    @staticmethod
    def calculate_basic_sales_tax(description):
        if Item.is_tax_exempted(description):
            return 0
        else:
            return Item.BASIC_TAX

    @staticmethod
    def is_tax_exempted(description):
        category = Item.good_category.classify(description)
        print "category = %s" % category
        if category in ["book", "med", "food"]:
            return True
        else:
            return False