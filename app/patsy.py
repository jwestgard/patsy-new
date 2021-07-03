#!/usr/bin/env python3

from sqlalchemy import create_engine
from classes import Asset, Inventory
import sys


def main():
     engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


if __name__ == "__main__":
    print(sys.argv[1])
    inv = Inventory(sys.argv[1])

    for asset in inv:
        print(asset)
