from collections import Counter


def longest_substring(s: str, k: int) -> int:
    if len(s) < k:
        return 0

    # Count frequency of each character
    freq = Counter(s)

    # Split string on characters that appear less than k times
    for char in freq:
        if freq[char] < k:
            # Recursively check each part
            return max(longest_substring(sub, k) for sub in s.split(char))

    # If all characters appear at least k times, the whole string is valid
    return len(s)


def test():
    assert longest_substring("aaabb", 3) == 3
    assert longest_substring("ababbc", 2) == 5
