from collections import defaultdict
from typing import Callable


def num_complete_subarrays_v1(nums: list[int]) -> int:
    uniques: int = len(set(nums))
    counts = 0
    left = 0
    for right in range(len(nums)):
        subarray = nums[left : right + 1]
        for l in range(1, len(subarray) + 1):
            if len(set(subarray[-l:])) == uniques:
                counts += 1

    return counts


def num_complete_subarrays_v2(nums: list[int]) -> int:
    uniques = len(set(nums))
    freq: defaultdict[int, int] = defaultdict(int)
    completes = 0
    left = 0

    for right in range(len(nums)):
        freq[nums[right]] += 1

        while len(freq) == uniques:
            completes += len(nums) - right

            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]

            left += 1

    return completes


import pytest


@pytest.mark.parametrize(
    "num_complete_subarrays", [num_complete_subarrays_v1, num_complete_subarrays_v2]
)
def test(num_complete_subarrays: Callable[[list[int]], int]):
    assert num_complete_subarrays([1, 2, 3, 4]) == 1
    assert num_complete_subarrays([1, 3, 1, 2, 2]) == 4
    assert num_complete_subarrays([5, 5, 5, 5]) == 10
