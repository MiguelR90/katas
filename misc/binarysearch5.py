def binarysearch(nums: list[int], target: int) -> int:
    def bs(left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return bs(mid + 1, right)
        else:
            return bs(left, mid - 1)

    return bs(0, len(nums) - 1)


def test_search():
    assert binarysearch([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binarysearch([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binarysearch([], 1) == -1
    assert binarysearch([1], 1) == 0
    assert binarysearch([1], 0) == -1


if __name__ == "__main__":
    test_search()
