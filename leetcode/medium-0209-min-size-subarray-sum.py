def minimal_len(nums: list[int], target: int) -> int:
    minimal: int = 0

    left: int = 0
    right: int = 0

    while right < len(nums):
        if sum(nums[left : right + 1]) < target:
            right += 1
        elif minimal:
            minimal = min(minimal, right - left + 1)
            left += 1
        else:
            minimal = right - left + 1
            left += 1

    return minimal


def test():
    assert minimal_len([2, 3, 1, 2, 4, 3], 7) == 2
    assert minimal_len([1, 4, 4], 4) == 1
    assert (
        minimal_len(
            [
                1,
                1,
                1,
                1,
                1,
                1,
                1,
                1,
            ],
            11,
        )
        == 0
    )
