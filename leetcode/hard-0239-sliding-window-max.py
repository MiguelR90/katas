def sliding_window(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    output: list[int] = []

    for i in range(n - k + 1):
        output.append(max(nums[i : i + k]))

    return output


def test():
    assert sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [
        3,
        3,
        5,
        5,
        6,
        7,
    ]
    assert sliding_window([1], 1) == [1]
