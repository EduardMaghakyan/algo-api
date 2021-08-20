from click.testing import CliRunner

from algo_api.algorithms import fib_iter
from algo_api.interface.cli.algorithms import fibonacci


def test_fibonacci_cli():
    input = 12
    runner = CliRunner()
    result = runner.invoke(fibonacci, [str(input)])
    assert result.exit_code == 0
    assert fib_iter(input) == int(
        result.output
    ), f"Got wrong result from cli for {input} got {result.output}"
