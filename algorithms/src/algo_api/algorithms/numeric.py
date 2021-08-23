from typing import Optional


def fib_iter(n: int) -> Optional[int]:
    if n is None or n < 0:
        return None

    first, second = 0, 1
    for _ in range(0, n):
        first, second = second, first + second

    return first


def ackermann(m: int, n: Optional[int]) -> Optional[int]:
    if m is None or n is None or m < 0 or n < 0:
        return None

    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


def factorial(n: Optional[int]) -> Optional[int]:
    if n is None or n < 0:
        return None

    if n < 2:
        return 1

    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f
