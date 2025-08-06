from itertools import combinations


def three_sum_original(nums: list[int], target: int) -> int:
    n: int = len(nums)
    closest: int = sum(nums[:3])  # assume there is at least 3 elements in the array

    for i in range(n):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n - 2):
                triplet_sum: int = sum((nums[i], nums[j], nums[k]))

                if diff := abs(triplet_sum - target) == 0:
                    return triplet_sum

                elif diff < abs(closest - target):
                    closest = triplet_sum

    return closest


def three_sum(nums: list[int], target: int) -> int:
    closest: int = sum(nums[:3])

    for i, j, k in combinations(nums, 3):
        triplet_sum: int = sum((nums[i], nums[j], nums[k]))

        if abs(triplet_sum - target) < abs(closest - target):
            closest = triplet_sum

    return closest


def test():
    assert three_sum_original([-1, 2, 1, -4], 1) == 2
    assert three_sum_original([0, 0, 0], 1) == 0

    assert three_sum([-1, 2, 1, -4], 1) == 2
    assert three_sum([0, 0, 0], 1) == 0
