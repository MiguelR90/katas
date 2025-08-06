def max_sum_v1(nums: list[int]) -> int:
    sums: list[int] = [0] * len(nums)
    i: int = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums) and nums[j - 1] < nums[j]:
            j += 1

        sums.append(sum(nums[i:j]))

        i = j

    return max(sums)


def max_sum(nums: list[int]) -> int:
    total: int = 0
    i: int = 0
    while i < len(nums):
        j: int = i + 1
        while j < len(nums) and nums[j - 1] < nums[j]:
            j += 1

        total = max(total, sum(nums[i:j]))
        i = j

    return total


def test():
    assert max_sum([10, 20, 30, 5, 10, 50]) == 65
    assert max_sum([10, 20, 30, 40, 50]) == 150
    assert max_sum([12, 17, 15, 13, 10, 11, 12]) == 33
    assert max_sum([5]) == 5
    assert max_sum([]) == 0


test()
