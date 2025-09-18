# DP: with top down memoization solution
def fibonacci_memo(n: int) -> int:
    memo = dict[int, int]()

    def fib(k: int) -> int:
        if k in memo:
            return memo[k]

        if k in (0, 1):
            return k

        memo[k] = fib(k - 2) + fib(k - 1)
        return memo[k]

    return fib(n)


# DP: with bottom up looping solution
def fibonacci_loop(n: int) -> int:
    if n in (0, 1):
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


from typing import Callable
import pytest


@pytest.mark.parametrize("fibonacci", [fibonacci_memo, fibonacci_loop])
def test(fibonacci: Callable[[int], int]):
    for i, ans in [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
    ]:
        assert fibonacci(i) == ans
