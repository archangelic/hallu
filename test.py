import hallu.hallu

import click
from click.testing import CliRunner

def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(hallu.hallu.cli)
    assert result.exit_code == 0
    assert result.output == "hallu y'all\n"

if __name__ == '__main__':
    test_hello_world()
