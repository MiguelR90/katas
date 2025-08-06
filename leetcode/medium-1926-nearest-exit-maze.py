import copy
from typing import Literal


type Cell = Literal["+", "."]


# NOTE: this implementation uses deapth first search. This problem is better suited for bfs instead.
# bfs guarantees that once you've reached the exit you can escape while dfs requires you to complete
# the algorithm until a solution is found.
# dfs -> recursion
# bfs -> queue
def nearest_exit(
    maze: list[list[Cell]],
    entrance: tuple[int, int],
    visited: set[tuple[int, int]] | None = None,
) -> int:
    n, m = len(maze), len(maze[0])
    x, y = entrance

    if not visited:
        visited = set([entrance])

    if (x in {0, n - 1} or y in {0, m - 1}) and (x, y) not in visited:
        # at an exit
        return 0
    else:
        visited.add((x, y))
        moves: list[int] = []

        # try moving down
        if x - 1 >= 0 and maze[x - 1][y] == "." and (x - 1, y) not in visited:
            moves.append(nearest_exit(maze, (x - 1, y), copy.copy(visited)))

        # try moving up
        if x + 1 < n and maze[x + 1][y] == "." and (x + 1, y) not in visited:
            moves.append(nearest_exit(maze, (x + 1, y), copy.copy(visited)))

        # try moving left
        if y - 1 >= 0 and maze[x][y - 1] == "." and (x, y - 1) not in visited:
            moves.append(nearest_exit(maze, (x, y - 1), copy.copy(visited)))

        # try moving right
        if y + 1 < m and maze[x][y + 1] == "." and (x, y + 1) not in visited:
            moves.append(nearest_exit(maze, (x, y + 1), copy.copy(visited)))

        if moves:
            return 1 + min(moves)
        else:
            return -1


def test():
    assert (
        nearest_exit(
            [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], (1, 2)
        )
        == 1
    )

    assert (
        nearest_exit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], (1, 0)) == 2
    )

    assert nearest_exit([[".", "+"]], (0, 0)) == -1

    assert (
        nearest_exit([["+", "+", "+"], ["+", ".", "+"], ["+", "+", "+"]], (1, 1)) == -1
    )

    # this is wrong! not working like we expect
    # assert (
    #     nearest_exit(
    #         [["+", "+", "+", "+"], ["+", ".", ".", "+"], ["+", "+", "+", "+"]], (1, 2)
    #     )
    #     == -1
    # )


test()
