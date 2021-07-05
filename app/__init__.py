import click

from .commands.load import load
from .commands.dump import dump
from .database import Database as Database


@click.group()
@click.option('--dbfile', '-d', default=':memory:', help='Path to database file.')
@click.pass_context
def cli(ctx, dbfile):
    ctx.obj = Database(dbfile)
    print(ctx.obj)


cli.add_command(load)
cli.add_command(dump)