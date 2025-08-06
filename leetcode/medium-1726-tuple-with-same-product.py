from itertools import product


def num_tuples_orig(nums: list[int]) -> int:
    count: int = 0

    for a in nums:
        for b in nums:
            for c in nums:
                for d in nums:
                    if len(set((a, b, c, d))) == 4 and a * b == c * d:
                        count += 1

    return count


def num_tuples(nums: list[int]) -> int:
    count: int = 0
    for a, b, c, d in product(*[nums] * 4):
        if len(set((a, b, c, d))) == 4 and a * b == c * d:
            count += 1

    return count


def test():
    assert num_tuples([2, 3, 4, 6]) == 8
    assert num_tuples([1, 2, 4, 5, 10]) == 16


test()
