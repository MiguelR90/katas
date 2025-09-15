from collections import Counter


def length_of_longest_substring_v1(s: str) -> int:
    left: int = 0
    counter: Counter[str] = Counter()
    longest: int = 0

    for right in range(len(s)):
        counter[s[right]] += 1

        while max(counter.values()) > 1:
            counter[s[left]] -= 1
            left += 1

        if (current := len(s[left : right + 1])) > longest:
            longest = current

    return longest


def length_of_longest_substring_v2(s: str) -> int:
    left: int = 0
    longest: int = 0
    seen: set[str] = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        longest = max(longest, right - left + 1)

    return longest


length_of_longest_substring = length_of_longest_substring_v2


def test_length_of_longest_substring():
    # LeetCode examples
    assert length_of_longest_substring_v1("abcabcbb") == 3
    assert length_of_longest_substring_v1("bbbbb") == 1
    assert length_of_longest_substring_v1("pwwkew") == 3

    # Edge cases
    assert length_of_longest_substring_v1("") == 0
    assert length_of_longest_substring_v1("a") == 1
    assert length_of_longest_substring_v1("au") == 2
    assert length_of_longest_substring_v1("dvdf") == 3

    # Mixed patterns
    assert length_of_longest_substring_v1("abba") == 2
    assert length_of_longest_substring_v1("anviaj") == 5
    assert length_of_longest_substring_v1("tmmzuxt") == 5
