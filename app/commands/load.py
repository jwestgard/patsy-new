import click
import sys

from sqlalchemy import insert

from ..classes.inventory import Inventory as Inventory


@click.command(help='Load records to the database.')
@click.option('--source', '-s', required=True, help='CSV file to load.')
@click.option('--batch', '-b', required=False, help='Batch to load assets into.')
@click.pass_obj
def load(database, source, batch=None):
    print(database.__dict__)
    print(f"Loading records from {source}...", file=sys.stderr)
    inventory = Inventory(source)
    print(inventory, file=sys.stderr)
    
    with database.engine.begin() as conn:
        print(conn)
        result = conn.execute(insert(database.assets_table), 
                    [asset for asset in inventory]
                    )
        conn.commit()
