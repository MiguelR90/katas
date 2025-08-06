def contains_duplicates(nums: list[int], k: int) -> bool:
    n: int = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if j - i > k:
                break

            if nums[i] == nums[j]:
                return True

    return False


def test():
    assert contains_duplicates([1, 2, 3, 1], 3) is True
    assert contains_duplicates([1, 0, 1, 1], 1) is True
    assert contains_duplicates([1, 2, 3, 1, 2, 3], 2) is False
