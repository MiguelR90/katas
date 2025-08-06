from __future__ import annotations
from dataclasses import dataclass, field
from typing import Self


@dataclass
class TrieNode:
    children: dict[str, TrieNode] = field(default_factory=dict)
    word: str | None = None

    def _add_word(self, word: str) -> Self:
        node = self
        for chr in word:
            node = node.children.setdefault(chr, TrieNode())
        node.word = word
        return self

    def build(self, words: list[str]) -> Self:
        for word in words:
            _ = self._add_word(word)
        return self

    def print(self, prefix: str = "", level: int = 0) -> None:
        indent = "  " * level
        if self.word:
            print(f"{indent}- {prefix} (word end)")
        for ch, child in self.children.items():
            print(f"{indent}- {prefix + ch}")
            child.print(prefix + ch, level + 1)


if __name__ == "__main__":
    TrieNode().build(["car", "cat", "cart"]).print()
