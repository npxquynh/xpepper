import re, os
import pdb
import utility

class GoodCategory():
    DATA_FOLDER = "./data/"
    DEFAULT_CATEGORY = "other"
    CATEGORY = ["food", "med", "book", "other"]

    classifier = dict()

    def __init__(self, data_folder = ""):
        if data_folder == "":
            data_folder = self.DATA_FOLDER

        for key in self.CATEGORY:
            file_path = os.path.join(data_folder, "%s.txt" % key)

            self.classifier[key] = set()
            if os.path.isfile(file_path):
                self.classifier[key] = utility.read_file(file_path)

    def classify(self, description):
        """
        Simple & naive way to classify goods based on their names
        """
        category = self.DEFAULT_CATEGORY

        tokens = re.split("[\s]+", description)

        for token in tokens:
            for (key, word_set) in self.classifier.iteritems():
                if token in word_set:
                    category = key
                    break

        return category



