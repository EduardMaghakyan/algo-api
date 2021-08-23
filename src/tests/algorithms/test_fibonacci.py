import pytest

from algo_api.algorithms import fib_iter, fib_rec


def fib_test_cases():
    data = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 3], [5, 5], [6, 8], [7, 13]]
    for row in data:
        yield row


@pytest.mark.parametrize(["n", "expected"], fib_test_cases())
def test_fib_rec(n, expected):
    got = fib_rec(n)
    assert expected == got, f"Expecting Fibonacci of {n} to be {expected}, got {got}"


@pytest.mark.parametrize(["n", "expected"], fib_test_cases())
def test_fib_iter(n, expected):
    got = fib_iter(n)
    assert expected == got, f"Expecting Fibonacci of {n} to be {expected}, got {got}"
