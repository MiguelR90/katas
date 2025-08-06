VOWELS: set[str] = set(v for v in "aeiou")


def max_num_vowels(s: str, k: int) -> int:
    if len(s) < k:
        raise ValueError(f"{k=} is less then {len(s)=}")

    # only one substring
    elif len(s) == k:
        return sum(v in VOWELS for v in s)

    max_vowels: int = 0
    for i in range(len(s) - k):
        if (v := sum(v in VOWELS for v in s[i : i + k])) > max_vowels:
            max_vowels = v

    return max_vowels


def test():
    assert max_num_vowels("abciiidef", 3) == 3
    assert max_num_vowels("aeiou", 2) == 2
    assert max_num_vowels("aeiou", 5) == 5
    assert max_num_vowels("leetcode", 3) == 2
