def contains_duplicates(nums: list[int], indexDiff: int, valueDiff: int) -> bool:
    n: int = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if j - i > indexDiff:
                break

            if abs(nums[i] - nums[j]) <= valueDiff:
                return True

    return False


def test():
    assert contains_duplicates([1, 2, 3, 1], 3, 0) is True
    assert contains_duplicates([1, 5, 9, 1, 5, 9], 2, 3) is False
