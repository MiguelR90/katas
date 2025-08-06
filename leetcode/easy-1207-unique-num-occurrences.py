from collections import Counter


def is_unique(arr: list[int]) -> bool:
    counts = Counter(arr)
    return len(set(counts.values())) == len(counts)


def test():
    assert is_unique([1, 2, 2, 1, 1, 3]) is True
    assert is_unique([1, 2]) is False
    assert is_unique([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) is True
