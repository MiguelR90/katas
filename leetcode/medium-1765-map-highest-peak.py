from collections import deque


def map(is_water: list[list[int]]) -> list[list[int]]:
    n: int = len(is_water)
    m: int = len(is_water[0])
    heights: list[list[int]] = [[-1] * m for _ in range(n)]
    queue: deque[tuple[int, int]] = deque()

    # init search from all the water sources
    for i in range(n):
        for j in range(m):
            if is_water[i][j] == 1:
                queue.append((i, j))
                heights[i][j] = 0

    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while queue:
        i, j = queue.popleft()
        for di, dj in directions:
            if (
                0 <= (ni := i + di) < n
                and 0 <= (nj := j + dj) < m
                and heights[ni][nj] == -1
            ):
                heights[ni][nj] = heights[i][j] + 1
                queue.append((ni, nj))

    return heights


def test():
    assert map([[0, 1], [0, 0]]) == [[1, 0], [2, 1]]
    assert map([[0, 0, 1], [1, 0, 0], [0, 0, 0]]) == [[1, 1, 0], [0, 1, 1], [1, 2, 2]]


test()
