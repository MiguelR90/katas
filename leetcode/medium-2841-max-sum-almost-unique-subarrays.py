"""
You are given an integer array nums and two positive integers m and k.

Return the maximum sum out of all almost unique subarrays of length k of nums. If no such subarray exists, return 0.

A subarray of nums is almost unique if it contains at least m distinct elements.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

from collections import Counter


def maxsum_of_almost_unique_subarray(nums: list[int], m: int, k: int) -> int:
    maxsum: int = 0
    cursum: int = sum(nums[:k])

    freq: Counter[int] = Counter(nums[:k])
    if len(freq) >= m:
        maxsum = max(maxsum, cursum)

    for i in range(k, len(nums)):
        cursum += nums[i] - nums[i - k]
        freq[nums[i]] += 1
        freq[nums[i - k]] -= 1

        # NOTE: important otherwise len(freq) calc is too larger
        if freq[nums[i - k]] == 0:
            del freq[nums[i - k]]

        if len(freq) >= m:
            maxsum = max(maxsum, cursum)

    return maxsum


def test():
    assert maxsum_of_almost_unique_subarray(nums=[2, 6, 7, 3, 1, 7], m=3, k=4) == 18
    assert maxsum_of_almost_unique_subarray(nums=[5, 9, 9, 2, 4, 5, 4], m=1, k=3) == 23
    assert maxsum_of_almost_unique_subarray(nums=[1, 2, 1, 2, 1, 2, 1], m=3, k=3) == 0


def main():
    _ = maxsum_of_almost_unique_subarray(nums=[2, 6, 7, 3, 1, 7], m=3, k=4)


if __name__ == "__main__":
    main()
