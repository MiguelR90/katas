def max_consecutive_ones(nums: list[int], k: int) -> int:
    maxones: int = 0
    for i in range(len(nums) - 1):
        for j in range(1, len(nums)):
            if (m := len(nums[i:j])) <= sum(nums[i:j]) + k and maxones < m:
                maxones = m

    return maxones


def test():
    assert max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert (
        max_consecutive_ones(
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
        )
        == 10
    )
