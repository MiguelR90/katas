def find_decision_index(grid: list[list[int]]) -> tuple[int, int]:
    index: int = 0
    points: int = 0

    for i in range(len(grid[0])):
        if points < (p := sum(grid[0][: i + 1]) + sum(grid[1][i:])):
            points = p
            index = i

    return index, points


def game(grid: list[list[int]]) -> int:
    index: int
    points: int

    # Robot 1 decision
    index, points = find_decision_index(grid)

    # Subracts robot 1 decision
    for i in range(index + 1):
        grid[0][i] = 0

    for i in range(index, len(grid[1])):
        grid[1][i] = 0

    # Robot 2 decision
    _, points = find_decision_index(grid)

    return points


def test():
    assert game([[2, 5, 4], [1, 5, 1]]) == 4
    assert game([[3, 3, 1], [8, 5, 2]]) == 4
    assert game([[1, 3, 1, 15], [1, 3, 3, 1]]) == 7


test()
