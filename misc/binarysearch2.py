def search_recursing(nums: list[int], target: int) -> int:
    def bs(left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return bs(left, mid - 1)
        else:
            return bs(mid + 1, right)

    return bs(0, len(nums) - 1)


def search_looping(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# search = search_recursing
search = search_looping


def test_bs():
    nums = [-1, 0, 3, 5, 9, 12]

    assert search(nums, 9) == 4
    assert search(nums, 0) == 1
    assert search(nums, -1) == 0
    assert search(nums, 12) == 5
    assert search(nums, 2) == -1
    assert search(nums, 13) == -1
    assert search([1], 1) == 0
    assert search([1], 0) == -1
