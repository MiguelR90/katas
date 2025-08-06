def has_triplet(nums: list[int]) -> bool:
    for i, a in enumerate(nums):
        for j, b in enumerate(nums[i + 1 :]):
            if a < b:
                for k, c in enumerate(nums[j + 1 :]):
                    if b < c:
                        return True

    return False


def has_triplet2(nums: list[int]) -> bool:
    # array is empty
    if not nums:
        return False

    i, j = 0, 0
    a, b = nums[i], nums[j]

    for k, c in enumerate(nums[1:], start=1):
        if (i < j < k) and (a < b < c):
            return True

        # in case of tie choose the earliest index
        elif c < a:
            i, a = k, c

        # in case of tie choose the latest index
        elif b <= c:
            j, b = k, c

    return False


def test():
    assert has_triplet2([1, 2, 3, 4, 5])
    assert not has_triplet2([5, 4, 3, 2, 1])
    assert has_triplet2([1, 1, 0, 1, 5, 4, 6, 3, 1, 2])
