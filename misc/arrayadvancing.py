from typing import Callable
import pytest


def reachable_backtracking(nums: list[int]) -> bool:
    def backtrack(i: int) -> bool:
        if i >= len(nums):
            return True

        for j in range(1, nums[i] + 1):
            if backtrack(i + j):
                return True

        return False

    return backtrack(0)


def reachable_looping(nums: list[int]) -> bool:
    current, furthest, last = 0, 0, len(nums) - 1

    while current <= furthest and current <= last:
        furthest = max(furthest, current + nums[current])
        current += 1

    return furthest >= last


@pytest.mark.parametrize("reachable", [reachable_backtracking, reachable_looping])
def test(reachable: Callable[[list[int]], bool]):
    assert reachable([3, 3, 1, 0, 2, 0, 1])
    assert not reachable([3, 2, 0, 0, 2, 0, 1])
