"""

Problem Statement

You are given an integer array nums and an integer k.
There is a sliding window of size k that moves from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return an array of the maximum values in each window.

"""


def sliding_window_fixed(nums: list[int], k: int) -> list[int]:
    if (n := len(nums)) < k:
        return []

    results: list[int] = []

    for i in range(n - k + 1):
        # NOTE: optimize by keeping a heap with deleted items
        # OPT: O(n * k) -> O(n * log(k))
        results.append(max(nums[i : i + k]))

    return results


def test():
    assert sliding_window_fixed([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_fixed([1], 1) == [1]
    assert sliding_window_fixed([9, 11], 2) == [11]
    assert sliding_window_fixed([4, -2], 1) == [4, -2]
    assert sliding_window_fixed([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5]
    assert sliding_window_fixed([10, 9, 8, 7, 6, 5], 2) == [10, 9, 8, 7, 6]
    assert sliding_window_fixed([1, 2, 3, 4, 5, 6], 6) == [6]
    assert sliding_window_fixed([1, 2, 3, 4, 5, 6], 2) == [2, 3, 4, 5, 6]
    assert sliding_window_fixed([1, 1, 1, 1], 2) == [1, 1, 1]
