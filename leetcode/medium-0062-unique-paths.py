"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
"""

from functools import lru_cache
from typing import Callable


def unique_paths_topdown(m: int, n: int) -> int:
    @lru_cache(maxsize=m * n)
    def dp(i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 1

        return dp(i - 1, j) + dp(i, j - 1)

    return dp(m - 1, n - 1)


def unique_paths_bottomup(m: int, n: int) -> int:
    tab: list[list[int]] = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            tab[i][j] = tab[i - 1][j] + tab[i][j - 1]

    return tab[m - 1][n - 1]


import pytest


@pytest.mark.parametrize("unique_paths", [unique_paths_topdown, unique_paths_bottomup])
def test(unique_paths: Callable[[int, int], int]):
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
