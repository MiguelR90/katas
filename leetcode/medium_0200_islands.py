from typing import Literal


type Grid = list[list[Literal["1", "0"]]]


def islands(grid: Grid) -> int:
    n: int = len(grid)
    m: int = len(grid[0])

    def dfs(grid: Grid, r: int, c: int) -> int:
        if not (0 <= r < n) or not (0 <= c < m) or grid[r][c] == "0":
            return 0

        grid[r][c] = "0"

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            _ = dfs(grid, nr, nc)  # ignore summations from connected components

        return 1

    count: int = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                count += dfs(grid, i, j)

    return count


def test():
    assert (
        islands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )

    assert (
        islands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )


test()
