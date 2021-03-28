#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

from click.testing import CliRunner

from {{cookiecutter.project_slug}}.cli import  {{ cookiecutter.project_slug }}_cli as cli


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "Console script for {{ cookiecutter.project_slug }}" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output

def test_hello():
    """Test the hello command."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ["hello", "Foo"])
    assert result.exit_code == 0
    assert "Hello Foo" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
