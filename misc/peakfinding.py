def peakfind(nums: list[int]) -> int:
    def bisect(left: int, right: int) -> int:
        if left == right:
            return left

        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            result = bisect(left, mid)
        else:
            result = bisect(mid + 1, right)

        return result

    return bisect(0, len(nums) - 1)


def test_peakfind():
    assert peakfind([1, 2, 3, 1]) == 2
    assert peakfind([1, 2, 1, 3, 5, 6, 4]) in {1, 5}  # multiple valid answers
    assert peakfind([1]) == 0
    assert peakfind([2, 1]) == 0
    assert peakfind([1, 2]) == 1
    print("All tests passed.")


if __name__ == "__main__":
    test_peakfind()
