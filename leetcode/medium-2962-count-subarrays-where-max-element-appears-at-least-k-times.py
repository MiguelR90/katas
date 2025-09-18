"""
You are given an integer array nums and a positive integer k.
Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
A subarray is a contiguous sequence of elements within an array.
"""

from collections import Counter


def count_subarrays(nums: list[int], k: int):
    total = 0
    left = 0
    freq = Counter[int]()

    for right in range(len(nums)):
        freq[nums[right]] += 1

        while freq[nums[right]] >= k:
            total += len(nums) - right
            freq[nums[left]] -= 1
            left += 1

    return total


def test():
    assert count_subarrays(nums=[1, 3, 2, 3, 3], k=2) == 6
    assert count_subarrays(nums=[1, 4, 2, 1], k=3) == 0
