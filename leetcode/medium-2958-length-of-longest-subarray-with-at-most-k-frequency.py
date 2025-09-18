"""
You are given an integer array nums and an integer k.

The frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less than or equal to k.

Return the length of the longest good subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

from collections import Counter


def longest_subarray_atmost_kfreq(nums: list[int], k: int) -> int:
    longest = 0
    freq: Counter[int] = Counter()

    left = 0
    for right in range(len(nums)):
        freq[nums[right]] += 1

        # NOTE: global max is unnecessary just check freq of last element added i.e., nums[right]
        while freq[nums[right]] > k:
            # while max(freq.values()) > k: # this makes it O(n^2) boo!
            freq[nums[left]] -= 1
            left += 1

        longest = max(longest, right - left + 1)

    return longest


def test():
    assert longest_subarray_atmost_kfreq(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2) == 6
    assert longest_subarray_atmost_kfreq(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1) == 2
    assert longest_subarray_atmost_kfreq(nums=[5, 5, 5, 5, 5, 5, 5], k=4) == 4
