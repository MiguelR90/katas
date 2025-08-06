from collections import deque


def rotting_oranges(grid: list[list[int]]) -> int:
    n: int = len(grid)
    m: int = len(grid[0])
    queue: deque[tuple[int, int, int]] = deque()
    visited: set[tuple[int, int]] = set()

    # init the queue with all rotten oranges
    for i, j in ((i, j) for i in range(n) for j in range(m)):
        if grid[i][j] == 2:
            queue.append((i, j, 0))
            visited.add((i, j))

    elapsed_mins: int = 0
    while queue:
        i, j, current_mins = queue.popleft()

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if (
                0 <= ni < n
                and 0 <= nj < m
                and (ni, nj) not in visited
                and grid[ni][nj] == 1
            ):
                queue.append((ni, nj, current_mins + 1))
                visited.add((ni, nj))
                elapsed_mins = max(elapsed_mins, current_mins + 1)

    if sum(grid[i][j] > 0 for i in range(n) for j in range(m)) == len(visited):
        return elapsed_mins
    else:
        return -1


def test():
    assert rotting_oranges([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert rotting_oranges([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert rotting_oranges([[0, 2]]) == 0


test()
