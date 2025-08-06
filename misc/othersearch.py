def search(nums: list[int], target: int) -> int:
    def bisect(left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if target < nums[mid]:
            result = bisect(left, mid - 1)
        elif nums[mid] < target:
            result = bisect(mid + 1, right)
        elif mid > 0 and nums[mid - 1] == target:
            result = bisect(left, mid - 1)
        else:
            result = mid

        return result

    return bisect(0, len(nums) - 1)


def test():
    assert search([1, 2, 2, 2, 3, 4], 2) == 1
    assert search([1, 2, 3, 4, 5], 3) == 2
    assert search([1, 1, 1, 1, 1], 1) == 0
    assert search([1, 3, 5, 7], 2) == -1
    assert search([], 5) == -1
    assert search([5], 5) == 0
    assert search([5], 4) == -1
    assert search([2, 4, 4, 4, 6, 6], 6) == 4
    assert search([1, 2, 2, 2, 3], 2) == 1  # multiple duplicates; first occurrence
    assert search([1, 1, 1, 1, 1], 1) == 0  # all same value
    assert search([1, 2, 3, 4, 5], 3) == 2  # unique value in middle
    assert search([1, 2, 3, 4, 5], 1) == 0  # first element
    assert search([1, 2, 3, 4, 5], 5) == 4  # last element
    assert search([1, 3, 5, 7], 4) == -1  # not found


if __name__ == "__main__":
    test()
