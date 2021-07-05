import click


@click.command(help='Dump records from the database.')
@click.pass_context
def dump(database):
    print("This is the dump command!")
    print(ctx.obj)