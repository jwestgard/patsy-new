import click
import sys

from ..classes.inventory import Inventory as Inventory


@click.command(help='Load records to the database.')
@click.option('--source', '-s', required=True, help='CSV file to load.')
@click.pass_context
def load(database, source):
    print(f"Loading records from {source}...", file=sys.stderr)
    inventory = Inventory(source)
    for asset in inventory:
        print(asset)