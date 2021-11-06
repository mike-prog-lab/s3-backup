import click
from .backup import backup
from .config import config


@click.group()
def cli():
    pass


cli.add_command(backup)
cli.add_command(config)
