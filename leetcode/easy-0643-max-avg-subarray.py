from math import isclose


def max_avg_subarray(nums: list[int], k: int) -> float:
    if len(nums) < k:
        raise ValueError("k is larger than the size of the array")

    elif len(nums) == k:
        # there is only one subgroup
        return sum(nums) / k

    avg: float = 0.0
    for i in range(len(nums) - k):
        if avg < (sg_avg := sum(nums[i : i + k]) / k):
            avg = sg_avg

    return avg


def test():
    assert isclose(max_avg_subarray([1, 12, -5, -6, 50, 3], 4), 12.75)
    assert isclose(max_avg_subarray([5, 0], 1), 5.0)
    assert isclose(max_avg_subarray([5], 1), 5.0)
