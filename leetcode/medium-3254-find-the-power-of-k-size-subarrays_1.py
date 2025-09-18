"""
You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all subarrays of nums of size k.
Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].
"""


def subarray_powers_naive(nums: list[int], k: int) -> list[int]:
    powers: list[int] = []

    for i in range(len(nums) - k + 1):
        for j in range(k - 1):
            if nums[i + j + 1] - nums[i + j] != 1:
                powers.append(-1)
                break
        else:
            powers.append(nums[i + k - 1])

    return powers


from collections import Counter


def subarray_powers_opt(nums: list[int], k: int) -> list[int]:
    powers: list[int] = []
    valid = Counter[bool]()

    for j in range(k - 1):
        valid[nums[j + 1] - nums[j] == 1] += 1

    if valid[True] == k - 1:
        powers.append(nums[k - 1])
    else:
        powers.append(-1)

    for i in range(k, len(nums)):
        valid[nums[i - k + 1] - nums[i - k] == 1] -= 1
        valid[nums[i] - nums[i - 1] == 1] += 1

        if valid[True] == k - 1:
            powers.append(nums[i])
        else:
            powers.append(-1)

    return powers


def subarray_powers_alt(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    if k == 1:
        # any single element subarray is valid, power = element itself
        return nums[:]

    powers: list[int] = []

    # count consecutive "+1" gaps in the first window
    valid = 0
    for j in range(k - 1):
        if nums[j + 1] - nums[j] == 1:
            valid += 1

    if valid == k - 1:
        powers.append(nums[k - 1])
    else:
        powers.append(-1)

    # slide the window
    for i in range(k, n):
        # remove the leftmost gap (between nums[i-k] and nums[i-k+1])
        if nums[i - k + 1] - nums[i - k] == 1:
            valid -= 1

        # add the new rightmost gap (between nums[i-1] and nums[i])
        if nums[i] - nums[i - 1] == 1:
            valid += 1

        if valid == k - 1:
            powers.append(nums[i])
        else:
            powers.append(-1)

    return powers


from typing import Callable
import pytest


@pytest.mark.parametrize(
    "subarray_powers", [subarray_powers_naive, subarray_powers_opt, subarray_powers_alt]
)
def test(subarray_powers: Callable[[list[int], int], int]):
    assert subarray_powers([1, 2, 3], 3) == [3]
    assert subarray_powers([1, 2, 3], 2) == [2, 3]
    assert subarray_powers([1, 2, 3, 4, 3, 2, 5], 3) == [3, 4, -1, -1, -1]
    assert subarray_powers([2, 2, 2, 2, 2], 4) == [-1, -1]
    assert subarray_powers([3, 2, 3, 2, 3, 2], 2) == [-1, 3, -1, 3, -1]
