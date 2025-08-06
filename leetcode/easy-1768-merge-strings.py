from itertools import zip_longest


def merge(word1: str, word2: str) -> str:
    out: list[str] = []

    for a, b in zip_longest(word1, word2):
        if a:
            out.append(a)
        if b:
            out.append(b)

    return "".join(out)


def test():
    assert merge("abc", "pqr") == "apbqcr"
    assert merge("ab", "pqrs") == "apbqrs"
    assert merge("abcd", "pq") == "apbqcd"
