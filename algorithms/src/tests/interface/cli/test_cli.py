from click.testing import CliRunner

from algo_api.algorithms import ackermann, factorial, fib_iter
from algo_api.interface.cli.algorithms import invoke_ackermann, invoke_factorial, invoke_fibonacci


def test_fibonacci_cli():
    input = 12
    runner = CliRunner()
    result = runner.invoke(invoke_fibonacci, [str(input)])
    assert result.exit_code == 0
    assert fib_iter(input) == int(
        result.output
    ), f"Got wrong result from cli for {input} got {result.output}"


def test_ackermann_cli():
    n = 3
    m = 1
    runner = CliRunner()
    result = runner.invoke(invoke_ackermann, [str(m), str(n)])
    assert result.exit_code == 0
    assert ackermann(m, n) == int(
        result.output
    ), f"Got wrong result from cli for {m, n} got {result.output}"


def test_factorial_cli():
    input = 12
    runner = CliRunner()
    result = runner.invoke(invoke_factorial, [str(input)])
    assert result.exit_code == 0
    assert factorial(input) == int(
        result.output
    ), f"Got wrong result from cli for {input} got {result.output}"
