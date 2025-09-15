"""
You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.
A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.
Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.
"""

from collections import Counter


def min_length_substr_v1(s: str) -> int:
    b: int = len(s) // 4  # okay -> len(s) is a multiple of 4
    balance: Counter[str] = Counter()
    left, right = 0, len(s) - 1

    while left <= right:
        if balance[s[left]] < b:
            balance[s[left]] += 1
            left += 1
        elif balance[s[right]] < b:
            balance[s[right]] += 1
            right -= 1
        else:
            break

    return right - left + 1


def min_length_substr_v2(s: str) -> int:
    target = len(s) // 4
    totals = Counter(s)
    excess = Counter({k: totals[k] - target for k in totals if totals[k] > target})

    if not excess:
        return 0

    left = 0
    counts: Counter[str] = Counter()
    smallest = len(s)

    for right in range(len(s)):
        counts[s[right]] += 1

        while excess <= counts:
            smallest = min(smallest, right - left + 1)
            counts[s[left]] -= 1
            left += 1

    return smallest


# min_length_substr = min_length_substr_v1
min_length_substr = min_length_substr_v2


def test():
    assert min_length_substr("QWER") == 0
    assert min_length_substr("QQWE") == 1
    assert min_length_substr("QQQW") == 2
    assert min_length_substr("QQQWWWEEERRR") == 0
    assert min_length_substr("QWER") == 0
    assert min_length_substr("QQWWEERR") == 0
    assert min_length_substr("QQWE") == 1
    assert min_length_substr("QWEQ") == 1
    assert min_length_substr("QWQE") == 1
    assert min_length_substr("QQQWWEER") == 1
    assert min_length_substr("QQWWWEER") == 1
    assert min_length_substr("QQQQ") == 3
    assert min_length_substr("QQWWWWWW") == 4
    assert min_length_substr("QQQQQWEE") == 3
    assert min_length_substr("QWQWQWQW") == 4
    assert min_length_substr("QQQWWERR") == 1
    assert min_length_substr("QQQQQWER") == 3
