from itertools import chain


def word_search_orig(board: list[list[str]], word: str) -> bool:
    n: int = len(board)
    m: int = len(board[0])

    def dfs(
        r: int,
        c: int,
        path: list[str] | None = None,
        visited: set[tuple[int, int]] | None = None,
    ) -> bool:
        if visited is None:
            visited = set([(r, c)])

        if path is None:
            path = [board[r][c]]

        # base case
        if "".join(path) == word:
            return True

        # recursive step
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < n
                and 0 <= nc < m
                and (nr, nc) not in visited
                and "".join(chain(path, [board[nr][nc]])) in word
            ):
                path.append(board[nr][nc])
                visited.add((nr, nc))
                return dfs(nr, nc, path, visited)

        return False

    for r, c in ((r, c) for r in range(n) for c in range(m)):
        if dfs(r, c):
            return True

    return False


def word_search(board: list[list[str]], word: str) -> bool:
    n: int = len(board)
    m: int = len(board[0])

    def dfs(r: int, c: int, index: int = 0) -> bool:
        # base-case
        if index == len(word):
            return True

        if not (0 <= r < n and 0 <= c < m and board[r][c] == word[index]):
            return False

        # recursive step
        tmp = board[r][c]
        board[r][c] = "#"
        index += 1

        if (
            dfs(r - 1, c, index)
            or dfs(r + 1, c, index)
            or dfs(r, c - 1, index)
            or dfs(r, c + 1, index)
        ):
            return True

        # backtracking
        board[r][c] = tmp

        return False

    return any(dfs(r, c) for r in range(n) for c in range(m) if board[r][c] == word[0])


def test():
    assert (
        word_search(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
        is True
    )
    assert (
        word_search(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
        )
        is True
    )
    assert (
        word_search(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
        )
        is False
    )


test()
