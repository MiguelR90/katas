"""
You are given a string s and an integer k.
Return the length of the longest substring that contains at most k distinct characters.
"""

from collections import Counter


def longest_substring_k_distinct(s: str, k: int) -> int:
    left: int = 0
    longest: int = 0
    freq: Counter[str] = Counter()

    for right in range(len(s)):
        freq[s[right]] += 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        longest = max(longest, right - left + 1)

    return longest


def test():
    assert longest_substring_k_distinct("eceba", 2) == 3  # "ece"
    assert longest_substring_k_distinct("aa", 1) == 2  # "aa"
    assert longest_substring_k_distinct("abcadcacacaca", 3) == 11
    assert longest_substring_k_distinct("abcabcabc", 2) == 2
    assert longest_substring_k_distinct("a", 1) == 1
    assert longest_substring_k_distinct("a", 2) == 1
    assert longest_substring_k_distinct("abaccc", 2) == 4  # "accc"
    assert longest_substring_k_distinct("", 2) == 0
