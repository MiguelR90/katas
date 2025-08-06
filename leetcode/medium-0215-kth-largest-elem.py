from heapq import heapify, heappop, nlargest


def kth_largest_v1(nums: list[int], k: int) -> int:
    _nums = [-n for n in nums]
    _ = heapify(_nums)

    for _ in range(k - 1):
        _ = heappop(_nums)

    return -_nums[0]


def kth_largest(nums: list[int], k: int) -> int:
    out = nlargest(k, nums)
    return out[-1]


def test():
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


test()
