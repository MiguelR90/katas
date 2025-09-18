"""
You are given an integer array nums. The uniqueness array of nums is the sorted array that contains the number of distinct elements of all the subarrays of nums. In other words, it is a sorted array consisting of distinct(nums[i..j]), for all 0 <= i <= j < nums.length.

Here, distinct(nums[i..j]) denotes the number of distinct elements in the subarray that starts at index i and ends at index j.

Return the median of the uniqueness array of nums.

Note that the median of an array is defined as the middle element of the array when it is sorted in non-decreasing order. If there are two choices for a median, the smaller of the two values is taken.
"""

from collections import Counter


def median_of_uniqueness_array(nums: list[int]) -> int:
    n = len(nums)
    maxdist = len(set(nums))
    freq = Counter[int]()

    for left in range(n):
        seen = set[int]()
        for right in range(left, n):
            seen.add(nums[right])
            freq[len(seen)] += 1

            # NOTE: no need to keep checking
            if len(seen) == maxdist:
                freq[maxdist] += n - right - 1
                break

    total = n * (n + 1) // 2
    mid = (total - 1) // 2

    cumfreq = 0
    for i in range(1, maxdist + 1):
        cumfreq += freq[i]

        # NOTE: cumfreq := freq and mid := index -> off by 1 -> string > compare
        if cumfreq > mid:
            return i

    raise RuntimeError("should never reach this line")


def test():
    assert median_of_uniqueness_array([1, 2, 3]) == 1
    assert median_of_uniqueness_array([3, 4, 3, 4, 5]) == 2
    assert median_of_uniqueness_array([4, 3, 5, 4]) == 2
