from itertools import combinations


def longest_harmonious(nums: list[int]) -> int:
    longest: int = 0

    for k in range(1, len(nums) + 1):
        # no reason to keep checking since there's no subseq prior that is harmonic
        if k - longest > 2:
            break

        for subs in combinations(nums, k):
            if max(subs) - min(subs) == 1:
                longest = len(subs)

                # no reason to keep checking for subs k
                break

    return longest


def test():
    assert longest_harmonious([1, 3, 2, 2, 5, 2, 3, 7]) == 5
    assert longest_harmonious([1, 2, 3, 4]) == 2
    assert longest_harmonious([1, 1, 1, 1]) == 0
