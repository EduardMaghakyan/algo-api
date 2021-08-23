import pytest

from algo_api.algorithms import factorial


def factorial_test_cases():
    data = [
        [None, None],
        [0, 1],
        [1, 1],
        [2, 2],
        [3, 6],
        [12, 479001600],
        [-12, None],
    ]
    for row in data:
        yield row


@pytest.mark.parametrize(["n", "expected"], factorial_test_cases())
def test_fib_rec(n, expected):
    got = factorial(n)
    assert expected == got, f"Expecting factorial of {n} to be {expected}, got {got}"
