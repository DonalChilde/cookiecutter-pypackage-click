"""Console script entry point for {{cookiecutter.project_slug}}."""

from logging import Logger
import sys
import click

from {{cookiecutter.project_slug}}.cli.example import hello
from {{cookiecutter.project_slug}}.app_config import LOGGER

logger = LOGGER

@click.group()
@click.pass_context
def main(ctx: click.Context, args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    # NOTE: as written, this code only runs when hello is called,
    # not when <entry point> --help is called. This is a group to
    # hold other commands and groups.
    ctx.obj = {}
    ctx.obj["important_value"] = {"key": "oh so important"}
    click.echo(
        "Replace this message by putting your code into "
        "{{cookiecutter.project_slug}}.cli.main"
    )
    click.echo(args)
    click.echo("See click documentation at https://click.palletsprojects.com/")
    logger.error("Just checking!")
    return 0


main.add_command(hello)
