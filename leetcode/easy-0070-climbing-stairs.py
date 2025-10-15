"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climbing_stairs_naive(n: int) -> int:
    if n in (1, 2):
        return n

    return climbing_stairs_naive(n - 2) + climbing_stairs_naive(n - 1)


def climbing_stairs_topdown(n: int) -> int:
    memo: dict[int, int] = {}

    def inner(k: int) -> int:
        if k in memo:
            return memo[k]

        if k in (1, 2):
            memo[k] = k
            return memo[k]

        return climbing_stairs_naive(k - 2) + climbing_stairs_naive(k - 1)

    return inner(n)


def climbing_stairs_bottomup(n: int) -> int:
    if n in (1, 2):
        return n

    prev, current = 1, 2

    for _ in range(3, n + 1):
        prev, current = current, prev + current

    return current


from typing import Callable
import pytest


@pytest.mark.parametrize(
    "climbing_stairs",
    [climbing_stairs_naive, climbing_stairs_topdown, climbing_stairs_bottomup],
)
def test(climbing_stairs: Callable[[int], int]):
    assert climbing_stairs(2) == 2
    assert climbing_stairs(3) == 3
    assert climbing_stairs(4) == 5
    assert climbing_stairs(5) == 8


"""
1

1 1 
2


1 2
1 1 1
2 1 


1 1 2
2 2
1 2 1
1 1 1 1
2 1 1

"""
