def dutchflag(nums: list[int], k: int):
    # nums[:smaller] -> nums[i] < k
    # nums[smaller:equal] -> nums[i] == k
    # nums[equal:larger] -> unclassified
    # nums[larger:] -> nums[i] > k
    smaller, equal, larger = 0, 0, len(nums)

    # while there are unclassified numbers iterate!!
    while equal < larger:
        if nums[equal] < k:
            nums[smaller], nums[equal] = nums[equal], nums[smaller]
            smaller += 1
            equal += 1
        elif nums[equal] == k:
            equal += 1
        else:
            larger -= 1
            nums[larger], nums[equal] = nums[equal], nums[larger]

    return smaller, larger


import pytest


@pytest.mark.parametrize(
    "nums, k, expected_left, expected_right",
    [
        ([3, 2, 2, 1, 4], 2, 1, 3),
        ([2, 2, 2], 2, 0, 3),
        ([5, 1, 2, 2, 3], 2, 1, 3),
        ([4, 5, 6], 5, 1, 2),
        ([6, 5, 4], 5, 1, 2),
    ],
)
def test_dutchflag(nums: list[int], k: int, expected_left: int, expected_right: int):
    left, right = dutchflag(nums, k)
    assert (left, right) == (expected_left, expected_right)
    assert all(n < k for n in nums[:left])
    assert all(n == k for n in nums[left:right])
    assert all(n > k for n in nums[right:])
