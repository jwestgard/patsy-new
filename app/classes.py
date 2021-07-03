from collections import UserList
import csv
import os


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


class Asset:

    def __init__(self, id, batch, sourcefile, sourceline, filename, bytes, timestamp,
                 storage_path):
        self.id = int(id)
        self.batch = batch
        self.sourcefile = sourcefile
        self.sourceline = int(sourceline)
        self.filename = filename
        self.bytes = int(bytes)
        self.timestamp = timestamp
        self.storage_path = storage_path

    def __repr__(self):
        return self.filename