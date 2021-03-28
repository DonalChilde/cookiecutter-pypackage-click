"""Console script entry point for {{cookiecutter.project_slug}}."""

import sys
import click
from {{cookiecutter.project_slug}}.cli.example import hello


@click.group()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo(
        "Replace this message by putting your code into "
        "{{cookiecutter.project_slug}}.cli.main"
    )
    click.echo(args)
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


main.add_command(hello)
