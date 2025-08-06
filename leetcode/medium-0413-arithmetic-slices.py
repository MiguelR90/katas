from collections.abc import Iterable


def generate_slices(nums: list[int], k: int) -> Iterable[list[int]]:
    for i in range(len(nums) - k + 1):
        yield nums[i : i + k]


def is_arithmetic(slice: list[int]) -> bool:
    diffs = set(j - i for i, j in zip(slice[:-1], slice[1:]))
    return len(diffs) == 1


def num_arithmetic(nums: list[int]) -> int:
    num_slices: int = 0

    for k in range(3, len(nums) + 1):
        for slice in generate_slices(nums, k):
            if is_arithmetic(slice):
                num_slices += 1

    return num_slices


def test():
    assert num_arithmetic([1, 2, 3, 4]) == 3
    assert num_arithmetic([1, 3, 5, 7, 9]) == 6
