import click


@click.command('upload')
def upload():
    """
    Upload file to backup provider.
    """
    click.echo('Uploading...')
