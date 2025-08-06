def three_sum(nums: list[int]) -> list[list[int]]:
    n: int = len(nums)
    out: list[list[int]] = []

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                triplet = sorted([nums[i], nums[j], nums[k]])
                if sum(triplet) == 0 and triplet not in out:
                    out.append(triplet)

    return sorted(out)


def test():
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
