def longest_subs_after_del_one(nums: list[int]) -> int:
    longest: int = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if len(nums[i:j]) - 1 <= (ll := sum(nums[i:j])) and longest < ll:
                longest = ll

    return longest


def test():
    assert longest_subs_after_del_one([1, 1, 0, 1]) == 3
    assert longest_subs_after_del_one([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
