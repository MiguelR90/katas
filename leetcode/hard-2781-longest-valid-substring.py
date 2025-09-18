from collections.abc import Iterable


def generate_substr(s: str, k: int) -> Iterable[str]:
    for i in range(len(s) - k + 1):
        yield s[i : i + k]


def longest_valid_substr_v1(word: str, forbidden: list[str]) -> int:
    longest = 0
    for k in range(len(word)):
        valid = False
        for sub in generate_substr(word, k):
            if all(f not in sub for f in forbidden):
                valid = True
                break

        if valid:
            longest = k
        else:
            break

    return longest


def longest_valid_substr_v2(word: str, forbidden: list[str]) -> int:
    forbidden_set = set(forbidden)
    n = len(word)

    def contians_forbidden(substr: str) -> bool:
        for fword in forbidden_set:
            if fword in substr:
                return True
        return False

    def is_valid(k: int) -> bool:
        # check all substrings of length k
        for i in range(n - k + 1):
            if not contians_forbidden(word[i : i + k]):
                return True

        return False

    left, right = 0, len(word)
    while left <= right:
        mid = (left + right) // 2

        if is_valid(mid):
            left = mid + 1
        else:
            right = mid - 1

    return left - 1


# longest_valid_substr = longest_valid_substr_v1
longest_valid_substr = longest_valid_substr_v2


def test():
    assert longest_valid_substr(word="leetcode", forbidden=["de", "le", "e"]) == 4
    assert longest_valid_substr(word="cbaaaabc", forbidden=["aaa", "cb"]) == 4
    assert longest_valid_substr("aaaaa", ["aa"]) == 1
    assert longest_valid_substr("abcabc", ["abc"]) == 4
    assert longest_valid_substr("ababab", ["aba"]) == 3
    assert longest_valid_substr("a", ["a"]) == 0
    assert longest_valid_substr("abcdefghijklmnopqrstuvwxy", ["zabc"]) == 25
    assert longest_valid_substr("abcdefghijklmnopqrstuvwxy", ["zabc", "abc"]) == 24


if __name__ == "__main__":
    longest_valid_substr(word="leetcode", forbidden=["de", "le", "e"])
