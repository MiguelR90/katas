def find_min(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    assert left == right
    return nums[left]


def test_find_min():
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11
    assert find_min([2, 3, 4, 5, 1]) == 1
    assert find_min([1]) == 1
    assert find_min([2, 1]) == 1
    assert find_min([5, 6, 1, 2, 3, 4]) == 1
    assert find_min([1, 2, 3, 4, 5]) == 1
