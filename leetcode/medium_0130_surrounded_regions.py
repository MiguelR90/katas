from typing import Literal


type Board = list[list[Literal["X", "O"]]]


def capture_original(board: Board) -> Board:
    # This implemenation doesn't work. I'm not sure why but the idea is to start at one of the edges
    # this is the opposite of what i originally tried to do
    n: int = len(board)
    m: int = len(board[0])

    def surrounded(
        board: Board, r: int, c: int, visited: set[tuple[int, int]] | None = None
    ) -> bool:
        if not visited:
            visited = set()

        # base-case 1: already captured
        if board[r][c] == "X":
            return True

        # base-case 2: edges cannot be surrounded
        if r in {0, n - 1} or c in {0, m - 1}:
            return False

        board[r][c] = "X"
        visited.add((r, c))

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and not surrounded(board, nr, nc, visited):
                board[r][c] = "O"
                return False

        return True

    for i in (i for i in range(n) if i not in {0, n - 1}):
        for j in (j for j in range(m) if j not in {0, m - 1}):
            if board[i][j] == "O":
                _ = surrounded(board, i, j)

    return board


def capture(board: Board) -> Board:
    n = len(board)
    m = len(board[0])

    def dfs(r: int, c: int):
        if r < 0 or r >= n or c < 0 or c >= m or board[r][c] != "O":
            return
        board[r][c] = "E"  # Mark as escape
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            dfs(r + dr, c + dc)

    # Step 1: Mark edge-connected 'O's
    for i in range(n):
        if board[i][0] == "O":
            dfs(i, 0)
        if board[i][m - 1] == "O":
            dfs(i, m - 1)
    for j in range(m):
        if board[0][j] == "O":
            dfs(0, j)
        if board[n - 1][j] == "O":
            dfs(n - 1, j)

    # Step 2: Flip surrounded 'O's to 'X'
    for i in range(n):
        for j in range(m):
            if board[i][j] == "O":
                board[i][j] = "X"
            elif board[i][j] == "E":
                board[i][j] = "O"

    return board


def test():
    assert capture(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    ) == [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]

    assert capture([["X"]]) == [["X"]]

    assert capture(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "O", "X"],
        ]
    ) == [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "O", "X"],
    ]


test()
