def find_pivot_index(nums: list[int]) -> int:
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1 :]):
            return i

    return -1


def test():
    assert find_pivot_index([1, 7, 3, 6, 5, 6]) == 3
    assert find_pivot_index([1, 2, 3]) == -1
    assert find_pivot_index([2, 1, -1]) == 0
    assert find_pivot_index([-1, 1, 2]) == 2
