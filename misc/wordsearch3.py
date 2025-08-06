from typing import Self


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.word: str | None = None

    def _add_word(self, word: str):
        node = self
        for chr in word:
            node = node.children.setdefault(chr, TrieNode())
        node.word = word

    def build(self, words: list[str]) -> Self:
        for word in words:
            self._add_word(word)

        return self


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    n, m = len(board), len(board[0])
    out: list[str] = []
    root: TrieNode = TrieNode().build(words)
    visited: list[list[bool]] = [[False] * m for _ in range(n)]

    def backtrack(i: int, j: int, node: TrieNode):
        if node.word:
            out.append(node.word)
            node.word = None  # prevents finding duplicated words

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if (
                0 <= ni < n
                and 0 <= nj < m
                and not visited[ni][nj]
                and (nchr := board[ni][nj]) in node.children
            ):
                visited[ni][nj] = True
                backtrack(ni, nj, node.children[nchr])
                visited[ni][nj] = False

    for i in range(n):
        for j in range(m):
            if (nchr := board[i][j]) in root.children:
                visited[i][j] = True
                backtrack(i, j, root.children[nchr])
                visited[i][j] = False

    return list(set(out))


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
    print(out)
    assert sorted(out) == sorted(["eat", "oath"])
