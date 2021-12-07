"""Console script entry point for {{cookiecutter.project_slug}}."""

from logging import Logger
import sys
import click

from ..cli.file_hash_cli import hasher_


logger = logger = Logger(__name__)


class App:
    def __init__(self, config, verbosity: int = 0) -> None:
        self.verbosity = verbosity
        self.config = config

    def __repr__(self):
        return f"<{self.__class__.__name__}: verbosity={self.verbosity}, config={self.config}"


@click.group()
@click.option("-v", "--verbose", multiple=True, is_flag=True)
@click.pass_context
def main(ctx: click.Context, verbose):
    """Console script for {{cookiecutter.project_slug}}."""
    # NOTE: as written, this code only runs when hello is called,
    # not when <entry point> --help is called. This is a group to
    # hold other commands and groups.
    init_ctx_obj(ctx, verbose)
    # Hello message
    # TODO make an About message
    click.echo("Cli Program v1.0")
    # click.echo(args)
    click.echo("See click documentation at https://click.palletsprojects.com/")
    logger.error("Just checking!")
    return 0


def init_ctx_obj(context: click.Context, verbose):
    context.obj = App({}, len(verbose))
    context.obj.config = {"key": "oh so important"}


main.add_command(hasher_)
