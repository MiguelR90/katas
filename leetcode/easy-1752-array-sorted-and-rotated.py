def check(nums: list[int]) -> bool:
    sort = sorted(nums)
    for i in range(len(nums)):
        if nums[i:] + nums[:i] == sort:
            return True

    return False


def test():
    assert check([3, 4, 5, 1, 2]) is True
    assert check([2, 1, 3, 4]) is False
    assert check([1, 2, 3]) is True


test()
