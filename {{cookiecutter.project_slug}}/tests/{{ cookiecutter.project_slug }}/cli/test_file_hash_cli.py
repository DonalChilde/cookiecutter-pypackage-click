"""Tests for `file_hash_cli` package."""

from {{cookiecutter.project_slug}}.cli.file_hash_cli import  main_cli as cli
from click.testing import CliRunner

# # The name of the CLI program using the file_hash_cli module.
# CLI_BASE = "{{cookiecutter.project_slug}}"

# # Use "hasher" if using the hasher click.group, and "" if using the individual click.commands
# # from file_hash_cli
# HASHER = "hasher"
# # HASHER = ""


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "File Hash" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message and exit." in help_result.output


def test_hash_file_with_md5():
    """Test hashing a file."""
    # TODO
    # * make a file on the fly in temp dir
    # * hash the file
    # * hash the test string.
    # * compare the hashes
    test_string = "this is a test."
    runner = CliRunner()
    result = runner.invoke(cli.main, ["hash", "md5", "-f", "path to test file here"])
    assert result.exit_code == 0
    assert "Hello Foo" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output


def test_hash_a_string():
    pass


def test_hash_all_the_files():
    pass


def test_hash_with_multiple_methods():
    pass
