"""An example of a click command."""
import click


@click.command()
@click.argument("name")
def hello(name):
    """Make a polite greeting"""
    click.echo(f"Hello {name}!")
