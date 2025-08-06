def search(board: list[list[str]], word: str) -> bool:
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]

    def backtrack(i: int, j: int, index: int) -> bool:
        if index == len(word) - 1:
            return True

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj

            if (
                0 <= ni < n
                and 0 <= nj < m
                and not visited[ni][nj]
                and board[ni][nj] == word[index + 1]
            ):
                visited[ni][nj] = True
                if backtrack(ni, nj, index + 1):
                    return True
                visited[ni][nj] = False

        return False

    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                visited[i][j] = True
                if backtrack(i, j, 0):
                    return True
                visited[i][j] = False

    return False


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    return [word for word in words if search(board, word)]


if __name__ == "__main__":
    out = find_words(
        board=[
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        words=["oath", "pea", "eat", "rain"],
    )
    assert sorted(out) == sorted(["eat", "oath"])
