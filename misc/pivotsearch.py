def findpivot(nums: list[int]) -> int:
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            return i

    return 0


def search(nums: list[int], target: int) -> int:
    def bisect(left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] > target:
            return bisect(left, mid - 1)
        elif nums[mid] < target:
            return bisect(mid + 1, right)
        else:
            return mid

    pivot = findpivot(nums)

    if (result := bisect(0, pivot - 1)) >= 0:
        return result

    if (result := bisect(pivot, len(nums) - 1)) >= 0:
        return result

    return -1


def test():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert search([1, 3], 3) == 1
    assert search([5, 6, 7, 8, 1, 2, 3, 4], 2) == 5
    assert search([6, 7, 8, 1, 2, 3, 4, 5], 8) == 2
    assert search([3, 1], 1) == 1
    assert search([1, 3], 1) == 0


if __name__ == "__main__":
    test()
