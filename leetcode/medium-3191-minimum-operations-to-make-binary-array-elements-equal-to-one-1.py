"""
You are given a binary array nums.

You can do the following operation on the array any number of times (possibly zero):

Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
"""


def min_number_of_operations(nums: list[int], k: int = 3) -> int:
    numops: int = 0

    for i in range(len(nums) - k + 1):
        if nums[i] == 0:
            numops += 1
            for j in range(k):
                nums[i + j] = 1 if nums[i + j] == 0 else 0

    if 0 in set(nums[-k:]):
        return -1

    return numops


def test():
    assert min_number_of_operations(nums=[0, 1, 1, 1, 0, 0]) == 3
    assert min_number_of_operations(nums=[0, 1, 1, 1]) == -1

    # Basic cases
    assert min_number_of_operations([1, 1, 1]) == 0  # already all 1s
    assert min_number_of_operations([0, 0, 0]) == 1  # flip once

    # Example from prompt
    assert min_number_of_operations([0, 1, 1, 1, 0, 0]) == 3

    # Small arrays
    assert min_number_of_operations([0]) == -1  # cannot flip single 0
    assert min_number_of_operations([1]) == 0  # already good
    assert min_number_of_operations([0, 1]) == -1  # cannot fix with k=3
    assert min_number_of_operations([1, 0]) == -1
    assert min_number_of_operations([0, 0, 1]) == -1
    assert min_number_of_operations([1, 0, 0]) == -1

    # Larger arrays
    assert min_number_of_operations([0, 0, 0, 0]) == -1  # not possible
    assert min_number_of_operations([1, 0, 1, 0, 1]) == -1
    assert min_number_of_operations([0, 0, 1, 0, 0, 1]) == 2

    # All zeros
    assert min_number_of_operations([0, 0, 0, 0, 0, 0]) == 2

    # Alternate patterns
    assert min_number_of_operations([0, 1, 0, 1, 0, 1]) == 3
    assert min_number_of_operations([1, 0, 1, 0, 1, 0]) == 3
