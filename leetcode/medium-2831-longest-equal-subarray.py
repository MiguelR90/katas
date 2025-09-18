def longest_equal_subarray(nums: list[int], k: int) -> int:
    longest = 0
    for target in set(nums):
        left = 0
        target_count = 0

        for right in range(len(nums)):
            if nums[right] == target:
                target_count += 1

            while (right - left + 1) - target_count > k:
                if nums[left] == target:
                    target_count -= 1
                left += 1

            longest = max(longest, target_count)

    return longest


def test():
    assert longest_equal_subarray([1, 3, 2, 3, 1, 3], 3) == 3
    assert longest_equal_subarray([1, 1, 2, 2, 1, 1], 2) == 4
    assert longest_equal_subarray([1, 3, 2, 3, 1, 3], 3) == 3
    assert longest_equal_subarray([1, 1, 2, 2, 5, 5], 2) == 2
    assert longest_equal_subarray([1, 1, 1, 1], 0) == 4
    assert longest_equal_subarray([1, 2, 3, 4], 0) == 1
    assert longest_equal_subarray([5], 1) == 1
    assert longest_equal_subarray([1, 2, 1], 2) == 2
