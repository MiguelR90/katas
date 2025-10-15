"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

from functools import lru_cache
from typing import Callable


def minimum_paths_topdown(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    @lru_cache(maxsize=m * n)
    def dp(i: int, j: int) -> int:
        if i == 0 and j == 0:
            return grid[0][0]
        elif i == 0:
            return dp(i, j - 1) + grid[i][j]
        elif j == 0:
            return dp(i - 1, j) + grid[i][j]

        return min(dp(i - 1, j), dp(i, j - 1)) + grid[i][j]

    return dp(m - 1, n - 1)


def minimum_paths_bottomup(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    tab: list[list[int]] = [[0] * n for _ in range(m)]

    tab[0][0] = grid[0][0]
    for i in range(1, m):
        tab[i][0] = tab[i - 1][0] + grid[i][0]

    for j in range(1, n):
        tab[0][j] = tab[0][j - 1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            tab[i][j] = min(tab[i - 1][j], tab[i][j - 1]) + grid[i][j]

    return tab[m - 1][n - 1]


import pytest


@pytest.mark.parametrize(
    "minimum_paths", [minimum_paths_topdown, minimum_paths_bottomup]
)
def test(minimum_paths: Callable[[list[list[int]]], int]):
    assert minimum_paths([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert minimum_paths([[1, 2, 3], [4, 5, 6]]) == 12
