def remove_duplicates(nums: list[int]) -> int:
    k: int = 0
    i: int = 0

    while i < len(nums):
        if nums[k] < nums[i]:
            k += 1
            nums[k], nums[i] = nums[i], nums[k]
        else:
            i += 1

    return k + 1


def test():
    assert remove_duplicates([1, 1, 2]) == 2
    assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    assert remove_duplicates([0, 1, 2, 4]) == 4
    assert remove_duplicates([0, 1, 2, 2]) == 3
