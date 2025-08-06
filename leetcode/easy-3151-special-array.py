def is_special(nums: list[int]) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] % 2 == nums[i + 1] % 2:
            return False

    return True


def test():
    assert is_special([1]) is True
    assert is_special([2, 1, 4]) is True
    assert is_special([4, 3, 1, 6]) is False


test()
