from collections import UserDict


class Asset(UserDict):

    def __init__(self, id, batch, sourcefile, sourceline, 
            filename, bytes, timestamp, storage_path
            ):
        super().__init__()
        self['batch'] = batch
        self['sourcefile'] = sourcefile
        self['sourceline'] = int(sourceline)
        self['filename'] = filename
        self['bytes'] = int(bytes)
        self['timestamp'] = timestamp
        self['storage_path'] = storage_path

    def __repr__(self):
        return self.filename
