"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""


def max_subarray_sum_naive(nums: list[int]) -> int:
    n = len(nums)
    maxsum = 0
    for i in range(n):
        cursum = 0
        for j in range(i, n):
            cursum += nums[j]
            maxsum = max(maxsum, cursum)
    return maxsum


def max_subarray_sum_memo(nums: list[int]) -> int:
    memo: dict[int, int] = {}

    def dp(i: int) -> int:
        if i in memo:
            return memo[i]

        if i == 0:
            memo[i] = nums[0]
            return memo[i]

        memo[i] = max(nums[i], dp(i - 1) + nums[i])
        return memo[i]

    return max(dp(i) for i in range(len(nums)))


def max_subarray_sum_tab(nums: list[int]) -> int:
    cursum = maxsum = nums[0]

    for i in range(1, len(nums)):
        cursum = max(cursum + nums[i], nums[i])
        maxsum = max(maxsum, cursum)

    return maxsum


from typing import Callable
import pytest


@pytest.mark.parametrize(
    "max_subarray_sum",
    [max_subarray_sum_naive, max_subarray_sum_memo, max_subarray_sum_tab],
)
def test(max_subarray_sum: Callable[[list[int]], int]):
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([1]) == 1
    assert max_subarray_sum([5, 4, -1, 7, 8]) == 23
