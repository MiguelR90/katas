from collections import Counter


def has_perm(s1: str, s2: str) -> bool:
    k: int = len(s1)
    target: Counter[str] = Counter(s1)

    for i in range(len(s2) - k + 1):
        if Counter(s2[i : i + k]) == target:
            return True

    return False


def test():
    assert has_perm("ab", "eidbaooo") is True
    assert has_perm("ab", "eidboaoo") is False
