import pdb

def read_file(file_name):
    word_set = set()

    with open(file_name) as file:
        for line in file:
            word_set.add(line.strip())

    return word_set