from collections import Counter


def anagrams(s: str, p: str) -> list[int]:
    out: list[int] = []
    k: int = len(p)
    p_count = Counter(p)

    for i in range(len(s) - k + 1):
        if Counter(s[i : i + k]) == p_count:
            out.append(i)

    return out


def test():
    assert anagrams("cbaebabacd", "abc") == [0, 6]
    assert anagrams("abab", "ab") == [0, 1, 2]
