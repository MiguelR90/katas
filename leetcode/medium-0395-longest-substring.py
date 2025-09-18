from collections import Counter


def longest_substring_v1(s: str, k: int) -> int:
    if len(s) < k:
        return 0

    # Count frequency of each character
    freq = Counter(s)

    # Split string on characters that appear less than k times
    for char in freq:
        if freq[char] < k:
            # Recursively check each part
            return max(longest_substring_v1(sub, k) for sub in s.split(char))

    # If all characters appear at least k times, the whole string is valid
    return len(s)


from collections import deque


def longest_substring_v2(s: str, k: int) -> int:
    queue: deque[str] = deque([s])
    longest: int = 0

    while queue:
        sub = queue.popleft()

        if len(sub) < k:
            continue

        freq = Counter(sub)

        if bad := next((ch for ch in freq if freq[ch] < k), None):
            queue.extend(sub.split(bad))
        else:
            longest = max(longest, len(sub))

    return longest


# longest_substring = longest_substring_v1
longest_substring = longest_substring_v2


def test():
    assert longest_substring("aaabb", 3) == 3
    assert longest_substring("ababbc", 2) == 5
    assert longest_substring("aaaaaa", 2) == 6
    assert longest_substring("abcdefg", 2) == 0
