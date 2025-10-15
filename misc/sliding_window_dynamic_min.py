"""

You are given two strings s and t.
Return the minimum window substring of s that contains all the characters of t. If there is no such substring, return an empty string "".

"""

from collections import Counter


def min_window(s: str, t: str) -> str:
    t_counts = Counter(t)
    s_counts: Counter[str] = Counter()

    left = 0
    sortest = ""

    for right in range(len(s)):
        s_counts[s[right]] += 1

        # NOTE: comparison is not very performant it can be improved by keeping a counter
        # and boolean array for the unique char that have been completed
        while t_counts <= s_counts:
            if not sortest or right - left + 1 < len(sortest):
                sortest = s[left : right + 1]

            s_counts[s[left]] -= 1
            if s_counts[s[left]] == 0:
                del s_counts[s[left]]
            left += 1

    return sortest


def test():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("ab", "b") == "b"
    assert min_window("ab", "a") == "a"
    assert min_window("aa", "aa") == "aa"
    assert min_window("bbaac", "aba") == "baa"
    assert min_window("abdecfab", "fab") == "fab"
    assert min_window("", "a") == ""
