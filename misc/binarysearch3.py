def search_recursion(nums: list[int], target: int) -> int:
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


def search_loop(nums: list[int], target: int) -> int:
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


# search = search_recursion
search = search_loop


def test_search():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([], 1) == -1
    assert search([1], 1) == 0
    assert search([1], 0) == -1


if __name__ == "__main__":
    test_search()
