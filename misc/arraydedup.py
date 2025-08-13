def dedup(nums: list[int]) -> int:
    write_index: int = 1

    for i in range(1, len(nums)):
        if nums[write_index - 1] != nums[i]:
            nums[write_index] = nums[i]
            write_index += 1

    return write_index


def test():
    assert dedup([1, 1, 2, 2, 3]) == 3
    assert dedup([1, 2, 3, 3, 3, 3]) == 3
    assert dedup([1, 1, 1, 1, 2, 3]) == 3
    assert dedup([1, 2, 2, 2, 2, 3, 4, 5, 6]) == 6
