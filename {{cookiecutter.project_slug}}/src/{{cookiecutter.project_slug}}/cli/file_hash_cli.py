from pathlib import Path
from typing import Optional

import click


from ..app_lib import file_hash


@click.group(name="hasher")
@click.pass_context
def hasher_(ctx: click.Context):
    pass


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
    click.echo(ctx)


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
    click.echo(ctx)
