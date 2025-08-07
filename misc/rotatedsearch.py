def find_pivot(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return left


def binary_search(nums: list[int], target: int, offset: int = 0) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return offset + mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def search_rotated(nums: list[int], target: int) -> int:
    pivot: int = find_pivot(nums)

    if target <= nums[-1]:
        return binary_search(nums[pivot:], target, pivot)
    else:
        return binary_search(nums[:pivot], target)


def test_search_rotated():
    assert find_pivot([4, 5, 6, 7, 0, 1, 2]) == 4

    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
    assert search_rotated([1], 1) == 0
    assert search_rotated([6, 7, 8, 1, 2, 3, 4, 5], 2) == 4
    assert search_rotated([5, 6, 7, 0, 1, 2, 3], 3) == 6
    assert search_rotated([1, 3], 3) == 1
