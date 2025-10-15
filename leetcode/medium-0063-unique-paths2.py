"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
"""

from functools import lru_cache
from typing import Callable


def unique_paths_topdown(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    @lru_cache(maxsize=m * n)
    def dp(i: int, j: int) -> int:
        if grid[i][j] == 1:
            return 0

        if i == 0 or j == 0:
            return 1

        return dp(i - 1, j) + dp(i, j - 1)

    return dp(m - 1, n - 1)


def unique_paths_bottomup(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    tab: list[list[int]] = [[1] * n for _ in range(m)]

    for i in (i for i in range(m) if grid[i][0] == 1):
        tab[i][0] = 0

    for j in (j for j in range(n) if grid[0][j] == 1):
        tab[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 1:
                tab[i][j] = 0
            else:
                tab[i][j] = tab[i - 1][j] + tab[i][j - 1]

    return tab[m - 1][n - 1]


import pytest


@pytest.mark.parametrize("unique_paths", [unique_paths_topdown, unique_paths_bottomup])
def test(unique_paths: Callable[[list[list[int]]], int]):
    assert unique_paths([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert unique_paths([[0, 1], [0, 0]]) == 1
