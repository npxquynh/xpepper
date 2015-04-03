import re, os, sys
from item import Item
from receipt import Receipt

def read_input(file_name):
    receipt = Receipt()

    print "INPUT"
    with open(file_name) as file:
        print "Input: %s" % file_name
        for line in file:
            print line.strip()
            quantity, description, price = parse_line(line.strip())
            receipt.add(quantity, description, price)

    print "OUTPUT"
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
    folder_path = "./input/"
    if len(sys.argv) != 0:
        folder_path = sys.argv[1]

    for f in os.listdir(folder_path):
        file_name = os.path.join(folder_path, f)
        read_input(file_name)