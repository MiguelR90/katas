import pytest


def rob(nums: list[int]) -> int:
    value: int = 0
    return value


@pytest.mark.skip
def test_rob():
    assert rob([1, 2, 3, 1]) == 4  # Rob house 1 and 3
    assert rob([2, 7, 9, 3, 1]) == 12  # Rob house 1, 3, 5
    assert rob([2, 1, 1, 2]) == 4  # Rob house 1 and 4
    assert rob([5, 5, 10, 100, 10, 5]) == 110
    assert rob([1]) == 1  # Only one house
    assert rob([]) == 0  # No houses
    assert rob([1, 3]) == 3  # Choose the bigger one
