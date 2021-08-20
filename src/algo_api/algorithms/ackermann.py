def acker(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    if n == 0:
        return acker(m - 1, 1)
    return acker(m - 1, acker(m, n - 1))
