def count(grid: list[list[int]]) -> int:
    n: int = len(grid)
    m: int = len(grid[0])
    connected: set[tuple[int, int]] = set()

    # row-wise
    for i in range(n):
        if sum(grid[i][j] for j in range(m)) < 2:
            continue

        for j in range(m):
            if grid[i][j]:
                connected.add((i, j))

    # col-wise
    for j in range(m):
        if sum(grid[i][j] for i in range(n)) < 2:
            continue

        for i in range(n):
            if grid[i][j]:
                connected.add((i, j))

    return len(connected)


def test():
    assert count([[1, 0], [0, 1]]) == 0
    assert count([[1, 0], [1, 1]]) == 3
    assert count([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) == 4


test()
