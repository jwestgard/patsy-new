from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import insert

import os


class Database(object):

    def __init__(self, dbfile=None):
        self.dbfile = dbfile
        self.engine = create_engine(
                f"sqlite+pysqlite:///{dbfile}", echo=True, future=True
                )
        self.metadata = MetaData()

        self.assets_table = Table(
            "assets", self.metadata,
            Column('id', Integer, primary_key=True),
            Column('batch', String(30)),
            Column('sourcefile', String),
            Column('sourceline', Integer),
            Column('filename', String),
            Column('bytes', Integer),
            Column('timestamp', String),
            Column('storage_path', String)
        )

        self.metadata.create_all(self.engine)

