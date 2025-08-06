from itertools import combinations


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    quads: list[list[int]] = []

    for q in combinations(nums, 4):
        quad: list[int] = sorted(q)

        if sum(quad) == target and quad not in quads:
            quads.append(quad)

    return sorted(quads)


def test():
    assert four_sum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ]
