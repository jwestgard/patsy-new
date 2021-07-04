import click
import os


class Database(object):
    def __init__(self, home=None, debug=False):
        self.home = os.path.abspath(home or '.')
        self.debug = debug


@click.group()
@click.option('--db-home', envvar='DATABASE_HOME', default='.db')
@click.option('--debug/--no-debug', default=False, envvar='REPO_DEBUG')
@click.pass_context
def main(ctx, repo_home, debug):
    ctx.obj = Repo(repo_home, debug)
    print("Hello CLI!")

