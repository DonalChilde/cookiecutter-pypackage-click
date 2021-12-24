from pathlib import Path
from typing import Optional
from logging import Logger

import click

# FIXME remove after dev
from ..app_lib import file_hash
from .cli_app import App

# from {{cookiecutter.project_slug}}.app_lib import file_hash

logger = logger = Logger(__name__)


# @click.group(name="hasher")
# @click.pass_context
# def hasher_(ctx: click.Context):
#     pass


@click.command(name="validate")
@click.argument("hex_digest", type=str, required=True)
@click.argument("hash_name", type=str, required=True)
@click.option(
    "-f", "--file_path", type=click.Path(exists=True, dir_okay=False, path_type=Path)
)
@click.option("-s", "--string", type=str)
@click.pass_context
def validate_(
    ctx: click.Context,
    hex_digest: str,
    hash_name: str,
    file_path: Optional[Path] = None,
    string: Optional[str] = None,
):
    # Check a file or string against a given digest and hash method.
    click.echo(str(ctx.params))
    click.echo(ctx.obj)


@click.command(name="hash")
@click.argument("hash_name", type=str, required=True)
@click.option(
    "-f", "--file_path", type=click.Path(exists=True, dir_okay=False, path_type=Path)
)
@click.option("-s", "--string", type=str)
@click.pass_context
def hash_(
    ctx: click.Context,
    hash_name: str,
    file_path: Optional[Path] = None,
    string: Optional[str] = None,
):
    # check for file or string
    # get hasher
    # calculate hash
    # display digest
    click.echo(str(ctx.params))
    click.echo(ctx.obj)


@click.group()
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Level of verbosity in output. Can be used multiple times.",
)
@click.pass_context
def main(ctx: click.Context, verbose):
    """File Hash"""

    init_ctx_obj(ctx, verbose)
    # Hello message
    # TODO make an About message

    return 0


def init_ctx_obj(context: click.Context, verbose):
    """Init the context.obj custom object."""
    context.obj = App({}, verbose)
    # context.obj.config = {"key": "oh so important"}


main.add_command(validate_)
main.add_command(hash_)
