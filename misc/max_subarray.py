def max_subarray_bottom_up(nums: list[int]) -> int:
    current: int = nums[0]
    gmax: int = current

    for i in range(1, len(nums)):
        current = max(current + nums[i], nums[i])
        if gmax < current:
            gmax = current

    return gmax


def max_subarray_top_down(nums: list[int]) -> int:
    memo: dict[int, int] = {0: nums[0]}

    def dp(i: int) -> int:
        if i not in memo:
            memo[i] = max(nums[i], nums[i] + dp(i - 1))

        return memo[i]

    for i in range(1, len(nums)):
        _ = dp(i)

    return max(memo.values())


# max_subarray = max_subarray_bottom_up
max_subarray = max_subarray_top_down


def test_max_subarray():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # [4, -1, 2, 1]
    assert max_subarray([1]) == 1  # single element
    assert max_subarray([5, 4, -1, 7, 8]) == 23  # full array
    assert max_subarray([-1, -2, -3, -4]) == -1  # all negative
    assert max_subarray([0, -3, 1, 1]) == 2  # [1, 1]
    assert max_subarray([1, 2, 3, -2, 5]) == 9  # [1, 2, 3, -2, 5]


if __name__ == "__main__":
    test_max_subarray()
