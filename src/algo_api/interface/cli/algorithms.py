import logging

import click

from algo_api import config
from algo_api.algorithms import acker, fib_iter

_LOG = logging.getLogger(__name__)


@click.group()
def main():
    config.setup_logger()


@click.command()
@click.argument("n", type=int, required=True)
def fibonacci(n: int):
    _LOG.info(f"Calculating Fibonacci of {n}")
    print(f"{fib_iter(int(n))}")


@click.command()
@click.argument("m", type=int, required=True)
@click.argument("n", type=int, required=True)
def ackermann(m: int, n: int):
    _LOG.info(f"Calculating Ackerman function of {m} and {n}")
    print(f"{acker(int(m), int(n))}")


main.add_command(fibonacci)
main.add_command(ackermann)
if __name__ == "__main__":
    main()
