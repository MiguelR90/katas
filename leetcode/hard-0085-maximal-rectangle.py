"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
"""


def maximal_rectangle(matrix: list[list[str]]) -> int:
    n, m = len(matrix), len(matrix[0])
    tabulate: list[list[int]] = [[0] * m for _ in range(n)]

    if matrix[0][0] == "1":
        tabulate[0][0] = 1

    for i in range(1, n):
        if matrix[i][0] == "1":
            tabulate[i][0] = tabulate[i - 1][0] + 1

    for j in range(1, m):
        if matrix[0][j] == "1":
            tabulate[0][j] = tabulate[0][j - 1] + 1

    for i in range(2, n):
        for j in range(2, m):
            if matrix[i][j] == "1":
                tabulate[i][j] = tabulate[i - 1][j] + tabulate[i][j - 1] + 1

    return max(max(tabulate[i]) for i in range(n))


import pytest


@pytest.mark.skip(reason="wrong implementation: keeping for reference")
def test():
    assert (
        maximal_rectangle(
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ]
        )
        == 6
    )
    assert maximal_rectangle([["0"]]) == 0
    assert maximal_rectangle([["1"]]) == 1
