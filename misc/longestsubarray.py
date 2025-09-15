def longest_subarray_twoloops(nums: list[int], k: int) -> int:
    longest: int = 0
    n: int = len(nums)

    for i in range(0, n):
        for j in range(i + 1, n + 1):
            if sum(nums[i:j]) <= k and (current_length := len(nums[i:j])) > longest:
                longest = current_length

    return longest


def longest_subarray_slidingwindow(nums: list[int], k: int) -> int:
    left, max_len, current_sum = 0, 0, 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > k:
            current_sum -= nums[left]
            left += 1

        if (current_len := right - left + 1) > max_len:
            max_len = current_len

    return max_len


# longest_subarray = longest_subarray_twoloops
longest_subarray = longest_subarray_slidingwindow


def test_longest_subarray_sum_leq_k():
    # Basic test
    nums = [1, 2, 3, 4, 5]
    k = 11
    assert longest_subarray(nums, k) == 4  # [2,3,4,5] exceeds, best is [1,2,3,4]

    # Exact sum equal to k
    nums = [2, 1, 5, 1, 1, 2]
    k = 8
    assert longest_subarray(nums, k) == 4  # [1,5,1,1]

    # Single element valid
    nums = [10, -5, 2, 3]
    k = 2
    assert longest_subarray(nums, k) == 3  # [-5,2]

    # All negatives
    nums = [-2, -3, -1, -4]
    k = -2
    assert longest_subarray(nums, k) == 4

    # No subarray satisfies condition
    nums = [5, 6, 7]
    k = 3
    assert longest_subarray(nums, k) == 0

    # Large window covers entire array
    nums = [1, 1, 1, 1, 1]
    k = 10
    assert longest_subarray(nums, k) == 5
