def len_of_longest(s: str) -> int:
    longest: int = 0
    left: int = 0
    sett: set[str] = set()

    for right in range(0, len(s)):
        while s[right] in sett:
            sett.remove(s[left])
            left += 1

        sett.add(s[right])
        longest = max(longest, right - left + 1)

    return longest


def test():
    assert len_of_longest("abcabcbb") == 3
    assert len_of_longest("bbbbb") == 1
    assert len_of_longest("pwwkew") == 3
