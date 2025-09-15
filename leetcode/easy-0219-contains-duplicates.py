"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from typing import Callable

import pytest


def contains_duplicates_v1(nums: list[int], k: int) -> bool:
    n: int = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if j - i > k:
                break

            if nums[i] == nums[j]:
                return True

    return False


def contains_duplicates_v2(nums: list[int], k: int) -> bool:
    left = 0
    seen: set[int] = set()

    for right in range(len(nums)):
        while right - left > k:
            seen.remove(nums[left])
            left += 1

        if nums[right] in seen:
            return True

        seen.add(nums[right])

    return False


@pytest.mark.parametrize("func", [contains_duplicates_v1, contains_duplicates_v2])
def test(func: Callable[[list[int], int], bool]):
    assert func([1, 2, 3, 1], 3) is True
    assert func([1, 0, 1, 1], 1) is True
    assert func([1, 2, 3, 1, 2, 3], 2) is False
