"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [nums[l], nums[l+1], ..., nums[r]] of which the sum is greater than or equal to target.
If there is no such subarray, return 0 instead."""


def min_subarray_len(nums: list[int], target: int) -> int:
    minlen, cursum, left = len(nums) + 1, 0, 0
    for right in range(len(nums)):
        cursum += nums[right]
        while cursum >= target:
            minlen = min(minlen, right - left + 1)
            cursum -= nums[left]
            left += 1

    # no subarray sum is greater than or equal to target
    if minlen > len(nums):
        return 0

    return minlen


def test():
    assert min_subarray_len([2, 3, 1, 2, 4, 3], 7) == 2  # [4,3]
    assert min_subarray_len([1, 4, 4], 4) == 1  # [4]
    assert min_subarray_len([1, 1, 1, 1, 1, 1, 1, 1], 11) == 0
    assert min_subarray_len([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15) == 2  # [10,7]
    assert min_subarray_len([1, 1], 3) == 0
    assert min_subarray_len([3], 3) == 1
    assert min_subarray_len([2, 3, 1, 2, 4, 3], 8) == 3  # [3,1,2,4]
