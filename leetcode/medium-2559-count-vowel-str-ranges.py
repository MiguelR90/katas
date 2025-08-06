vowels: frozenset[str] = frozenset(("a", "e", "i", "o", "u"))


def count_vowels(words: list[str], queries: list[list[int]]) -> list[int]:
    checks: list[bool] = [w[0] in vowels and w[-1] in vowels for w in words]

    ans: list[int] = []
    for right, left in queries:
        val = sum(c for c in checks[right : left + 1])
        ans.append(val)

    return ans


def test():
    assert count_vowels(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]) == [
        2,
        3,
        0,
    ]

    assert count_vowels(["a", "e", "i"], [[0, 2], [0, 1], [2, 2]]) == [3, 2, 1]


test()
