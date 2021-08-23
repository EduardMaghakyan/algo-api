import logging

import click

from algo_api import config
from algo_api.algorithms import ackermann, factorial, fib_iter

_LOG = logging.getLogger(__name__)


@click.group()
def main():
    config.setup_logger()


@click.command()
@click.argument("n", type=int, required=True)
def invoke_fibonacci(n: int):
    _LOG.info(f"Calculating Fibonacci of {n}")
    print(f"{fib_iter(int(n))}")


@click.command()
@click.argument("m", type=int, required=True)
@click.argument("n", type=int, required=True)
def invoke_ackermann(m: int, n: int):
    _LOG.info(f"Calculating Ackerman function of {m} and {n}")
    print(f"{ackermann(int(m), int(n))}")


@click.command()
@click.argument("n", type=int, required=True)
def invoke_factorial(n: int):
    _LOG.info(f"Calculating factorial of {n}")
    print(f"{factorial(int(n))}")


main.add_command(invoke_fibonacci, "fibonacci")
main.add_command(invoke_ackermann, "ackerman")
main.add_command(invoke_factorial, "factorial")
if __name__ == "__main__":
    main()
