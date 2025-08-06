def unique_paths_backtracking(m: int, n: int) -> int:
    def backtracking(i: int, j: int) -> int:
        if i == (m - 1) and j == (n - 1):
            return 1

        paths: int = 0
        for di, dj in [(0, 1), (1, 0)]:
            ni, nj = i + di, j + dj
            if ni < m and nj < n:
                paths += backtracking(ni, nj)

        return paths

    return backtracking(0, 0)


def unique_paths_top_down(m: int, n: int) -> int:
    memo: dict[tuple[int, int], int] = {}

    def dp(i: int, j: int):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 1 or j == 1:
            memo[(i, j)] = 1
            return memo[(i, j)]

        memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
        return memo[(i, j)]

    return dp(m, n)


def unique_paths_bottom_up(m: int, n: int) -> int:
    tabulate: list[list[int]] = [[0] * n for _ in range(m)]

    for i in range(m):
        tabulate[i][0] = 1

    for j in range(n):
        tabulate[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            tabulate[i][j] = tabulate[i - 1][j] + tabulate[i][j - 1]

    return tabulate[m - 1][n - 1]


# unique_paths = unique_paths_backtracking
# unique_paths = unique_paths_top_down
unique_paths = unique_paths_bottom_up


def test_unique_paths():
    assert unique_paths(3, 2) == 3  # Paths: RRD, RDR, DRR
    assert unique_paths(7, 3) == 28  # Larger grid
    assert unique_paths(1, 1) == 1  # Only one cell
    assert unique_paths(2, 2) == 2  # RD or DR
    assert unique_paths(10, 1) == 1  # Only one way: all down
    assert unique_paths(1, 10) == 1  # Only one way: all right
    assert unique_paths(10, 10) == 48620  # Stress test
