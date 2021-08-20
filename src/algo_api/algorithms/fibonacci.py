def fib_rec(n: int) -> int:
    if n < 2:
        return n

    return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iter(n: int) -> int:
    first, second = 0, 1
    for _ in range(0, n):
        first, second = second, first + second

    return first
