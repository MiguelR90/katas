def rotatedarray(nums: list[int]) -> int:
    def bisect(left: int, right: int) -> int:
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            result = bisect(mid + 1, right)
        else:
            result = bisect(left, mid)

        return result

    return bisect(0, len(nums) - 1)


def test_rotatedarray():
    assert rotatedarray([3, 4, 5, 1, 2]) == 1
    assert rotatedarray([4, 5, 6, 7, 0, 1, 2]) == 0
    assert rotatedarray([11, 13, 15, 17]) == 11
    assert rotatedarray([2, 1]) == 1
    assert rotatedarray([1]) == 1
    assert rotatedarray([2, 3, 4, 5, 6, 1]) == 1

    # more test cases
    assert rotatedarray([5, 1, 2, 3, 4]) == 1
    assert rotatedarray([1, 2, 3, 4, 5]) == 1  # not rotated
    assert rotatedarray([2, 3, 4, 5, 6, 7, 1]) == 1
    assert rotatedarray([6, 7, 1, 2, 3, 4, 5]) == 1
    assert rotatedarray([1, 2]) == 1
    assert rotatedarray([2, 3, 1]) == 1
    assert rotatedarray([9, 1, 2, 3, 4, 5, 6, 7, 8]) == 1
    assert rotatedarray([10, 11, 12, 1, 2, 3, 4, 5, 6]) == 1
    assert rotatedarray([2, 3, 4, 5, 6, 7, 8, 9, 1]) == 1


if __name__ == "__main__":
    test_rotatedarray()
