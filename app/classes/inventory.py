from collections import UserList
import csv
import os

from .asset import Asset as Asset


class Inventory(UserList):

    def __init__(self, path):
        super().__init__()
        self.filename = os.path.basename(path)
        self.path = path
        self.read()

    def read(self):
        with open(self.path) as handle:
            for row in csv.reader(handle):
                asset = Asset(*row)
                self.append(asset)

    def __repr__(self):
        return f"Inventory {self.filename} with {len(self)} items"