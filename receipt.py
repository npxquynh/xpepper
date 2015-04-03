from item import Item

class Receipt():
    _total = None
    _sales_tax = None

    def __init__(self):
        self.number_of_items = 0


        self.quantity = []
        self.description = []
        self.price = []
        self.tax = []
        pass

    def add(self, quantity, description, price):
        tax = Item.calculate_tax(description)

        self.number_of_items += 1
        self.quantity.append(quantity)
        self.description.append(description)
        self.price.append(price)
        self.tax.append(tax)

    def calculate_final_price(self, position):
        return self.price[position] + self._round(self.price[position] * self.tax[position], 0.05)

    def _round(self, number, round_to):
        """
        round to the nearest 0.05
        """
        return round_to * round(number / round_to, 0)

    def __str__(self):
        s = ""
        for i in range(self.number_of_items):
            s += ("%d %s: %.2f\n" % (
                self.quantity[i],
                self.description[i],
                self.calculate_final_price(i)
            ))


        s += ("Sales Taxes: %.2f\n" % self.get_sales_tax())
        s += ("Total: %.2f\n" % self.get_total())

        return s

    def get_sales_tax(self):
        if self._sales_tax is None:
            self._sales_tax = 0

            for i in range(self.number_of_items):
                self._sales_tax += round(self.price[i] * self.tax[i], 2)

        return self._sales_tax

    def get_total(self):
        if self._total is None:
            self._total = sum(self.price)
            self._total += self.get_sales_tax()

        return self._total

if __name__ == "__main__":
    receipt = Receipt()
    receipt.add(1, "milk", 3)
    receipt.__print__()
