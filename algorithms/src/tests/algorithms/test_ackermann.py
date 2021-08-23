import pytest

from algo_api.algorithms import ackermann


def ackerman_test_cases():
    data = [
        [1, 2, 4],
        [1, 3, 5],
        [1, 4, 6],
        [2, 2, 7],
        [2, 3, 9],
        [3, 4, 125],
        [-1, 4, None],
        [1, -4, None],
        [None, 4, None],
        [1, None, None],
    ]
    for row in data:
        yield row


@pytest.mark.parametrize(["m", "n", "expected"], ackerman_test_cases())
def test_fib_rec(m, n, expected):
    got = ackermann(m, n)
    assert expected == got, f"Expecting Ackerman of {m, n} to be {expected}, got {got}"
