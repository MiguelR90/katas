def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    for i, a in enumerate(nums[:-1]):
        for j, b in enumerate(nums[i + 1 :], start=i + 1):
            if a + b == target:
                return (i, j)


def test():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([3, 2, 4], 6) == (1, 2)
    assert two_sum([3, 3], 6) == (0, 1)
