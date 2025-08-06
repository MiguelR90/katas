def search(nums: list[int], target: int) -> int:
    def bisect(left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if target < nums[mid]:
            return bisect(left, mid - 1)
        elif nums[mid] < target:
            return bisect(mid + 1, right)
        else:
            return mid

    return bisect(0, len(nums) - 1)


def test_search():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([], 1) == -1
    assert search([1], 1) == 0
    assert search([1], 0) == -1


if __name__ == "__main__":
    test_search()
