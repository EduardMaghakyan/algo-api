import logging

import click

from algo_api import config
from algo_api.algorithms.fibonacci import fib_iter

_LOG = logging.getLogger(__name__)


@click.group()
def main():
    config.setup_logger()


@click.command()
@click.argument("n", type=int, required=True)
def fibonacci(n: int):
    _LOG.info(f"Calculating fibonacci of {n}")
    print(f"{fib_iter(int(n))}")


main.add_command(fibonacci)
if __name__ == "__main__":
    main()
