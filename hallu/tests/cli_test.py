import hallu.hallu

import click
from click.testing import CliRunner

import os

def test_no_args():
    runner = CliRunner()
    result = runner.invoke(hallu.hallu.cli)
    assert result.exit_code == 0
    assert result.output == "hallu y'all\n"

def test_init_no_args():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(hallu.hallu.cli, ['init'], input="test_run\n")
        assert result.exit_code == 0
        assert result.output.split('\n')[-2] == 'Project: "test_run" successfully initiated'
        assert 'settings.py' in os.listdir(os.getcwd())
        with open('settings.py', 'r') as s:
            assert s.read() == 'NAME = "test_run"\n'

