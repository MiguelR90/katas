from collections import Counter


def min_len(s: str) -> int:
    counter: Counter[str] = Counter(s)

    for letter in counter:
        while counter[letter] > 2:
            counter.subtract({letter: 2})

    return sum(c for c in counter.values())


def test():
    assert min_len("abaacbcbb") == 5
    assert min_len("aa") == 2
    assert min_len("ddaaabbbcccddde") == 5


test()
