from statistics import mean


def sliding_median(nums: list[int], k: int) -> list[int | float]:
    medians: list[int | float] = []

    for i in range(len(nums) - k + 1):
        window = sorted(nums[i : i + k])

        if k % 2 == 0:
            medians.append(mean(window[k // 2 : k // 2 + 2]))
        else:
            medians.append(window[k // 2])

    return medians


def test():
    assert sliding_median([1, 3, -1, -3, 5, 3, 6, 7], 3) == [1, -1, -1, 3, 5, 6]
    assert sliding_median([1, 2, 3, 4, 2, 3, 1, 4, 2], 3) == [2, 3, 3, 3, 2, 3, 2]
