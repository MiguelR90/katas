import sys


def max_subarray_sum_k_v1(nums: list[int], k: int) -> int:
    maxsum: int = -sys.maxsize - 1

    for i in range(len(nums) - k + 1):
        maxsum = max(maxsum, sum(nums[i : i + k]))

    return maxsum


def max_subarray_sum_k_v2(nums: list[int], k: int) -> int:
    cursum = sum(nums[:k])
    maxsum = cursum

    for i in range(k, len(nums)):
        cursum += nums[i]
        cursum -= nums[i - k]
        maxsum = max(maxsum, cursum)

    return maxsum


# max_subarray_sum_k = max_subarray_sum_k_v1
max_subarray_sum_k = max_subarray_sum_k_v2


def test_max_subarray_sum_k():
    # Basic examples
    assert max_subarray_sum_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_subarray_sum_k([2, 3, 4, 1, 5], 2) == 7

    # Edge cases
    assert max_subarray_sum_k([1, 2, 3, 4, 5], 5) == 15
    assert max_subarray_sum_k([1, 2, 3, 4, 5], 1) == 5
    assert max_subarray_sum_k([-1, -2, -3, -4], 2) == -3

    # Mixed numbers
    assert max_subarray_sum_k([4, -1, 2, 1, -5, 4], 2) == 3
    assert max_subarray_sum_k([1, -2, 3, -1, 2], 2) == 2


if __name__ == "__main__":
    max_subarray_sum_k([2, 1, 5, 1, 3, 2], 3)
    max_subarray_sum_k([2, 3, 4, 1, 5], 2)
