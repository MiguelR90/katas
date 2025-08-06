def remove_elements(nums: list[int], val: int) -> int:
    i: int = 0
    k: int = 0

    while i < len(nums):
        if k >= i:
            i += 1
        elif nums[i] != val:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
        else:
            i += 1

    return k


def test():
    assert remove_elements([3, 2, 2, 3], 3) == 2
    assert remove_elements([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
