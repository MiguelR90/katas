import itertools
import operator
from copy import copy


def move_zeros(nums: list[int]) -> list[int]:
    # this is O(n) memory i.e, not in place
    return list(
        itertools.chain(filter(operator.truth, nums), filter(operator.not_, nums))
    )


def move_zeros2(nums: list[int]) -> list[int]:
    for i in range(len(nums) - 1):
        if nums[i] != 0:
            continue

        for j in range(i + 1, len(nums)):
            if nums[j] == 0:
                continue

            nums[i], nums[j] = nums[j], nums[i]
            break  # otherwise they'll be in reverse order

    return nums


def test():
    assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeros2([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

    out = [1, 3, 4, 5, 0, 9, 0, 90, 90, 5, 60, 6, 0, 5]
    assert move_zeros(copy(out)) == move_zeros2(copy(out))
