import re
from item import Item
from receipt import Receipt

def read_input(file_name):
    receipt = Receipt()

    with open(file_name) as file:
        for line in file:
            quantity, description, price = parse_line(line.strip())
            receipt.add(quantity, description, price)

    print receipt

def parse_line(str):
    pattern = "(\d+)([\w\W]+)at\s(\d+\.\d+|\d+)"
    matched = re.match(pattern, str)

    if matched:
        quantity = int(matched.group(1))
        description = matched.group(2).strip()
        price = float(matched.group(3))

    return quantity, description, price

if __name__ == "__main__":
    read_input("./input/input1.txt")
    read_input("./input/input2.txt")
    read_input("./input/input3.txt")