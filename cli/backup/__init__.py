import click
from .commands import upload


@click.group('backup')
def backup():
    """
    Commands that interact with backup providers
    to store, update, download backups.
    """
    pass


backup.add_command(upload)
