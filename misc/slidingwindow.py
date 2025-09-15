"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""


def min_size_subarray_sum(nums: list[int], target: int) -> int:
    minsize = len(nums) + 1  # some arbitrary large number
    left = 0
    cursum = 0
    for right in range(len(nums)):
        cursum += nums[right]
        while cursum >= target:
            minsize = min(minsize, right - left + 1)
            cursum -= nums[left]
            left += 1

    # no subsequence exists
    if minsize > len(nums):
        return 0

    return minsize


def test():
    assert min_size_subarray_sum(nums=[2, 3, 1, 2, 4, 3], target=7) == 2
    assert min_size_subarray_sum(nums=[1, 4, 4], target=4) == 1
    assert min_size_subarray_sum(nums=[1, 1, 1, 1, 1, 1, 1, 1], target=11) == 0
