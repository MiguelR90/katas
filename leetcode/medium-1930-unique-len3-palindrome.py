def unique_palindrome(s: str) -> int:
    pals: set[tuple[str, str, str]] = set()

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                if s[i] == s[k]:
                    pals.add((s[i], s[j], s[k]))

    return len(pals)


def test():
    assert unique_palindrome("aabca") == 3
    assert unique_palindrome("adc") == 0
    assert unique_palindrome("bbcbaba") == 4
