from collections.abc import Iterable
from itertools import combinations, chain, pairwise


def powerset(n: int) -> Iterable[tuple[int, ...]]:
    yield from chain.from_iterable((combinations(range(n), r) for r in range(n + 1)))


def valid(subset: tuple[int, ...]) -> bool:
    for i, j in pairwise(subset):
        if abs(i - j) < 2:
            return False

    return True


def rob(nums: list[int]) -> int:
    value: int = 0
    for subset in powerset(len(nums)):
        if valid(subset):
            value = max(value, sum(nums[i] for i in subset))
    return value


def test_rob():
    assert rob([1, 2, 3, 1]) == 4  # Rob house 1 and 3
    assert rob([2, 7, 9, 3, 1]) == 12  # Rob house 1, 3, 5
    assert rob([2, 1, 1, 2]) == 4  # Rob house 1 and 4
    assert rob([5, 5, 10, 100, 10, 5]) == 110
    assert rob([1]) == 1  # Only one house
    assert rob([]) == 0  # No houses
    assert rob([1, 3]) == 3  # Choose the bigger one
