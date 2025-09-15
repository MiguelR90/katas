"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
"""


def num_nice_subarrays_v1(nums: list[int], k: int) -> int:
    """
    Count subarrays with exactly k odd numbers.
    Key insight: Use helper function to count subarrays with AT MOST k odd numbers.
    Answer = atMost(k) - atMost(k-1)
    """

    def at_most_k_odds(k: int) -> int:
        if k < 0:
            return 0

        left = 0
        odds = 0
        count = 0

        for right in range(len(nums)):
            odds += nums[right] % 2

            # Shrink window until we have at most k odd numbers
            while odds > k:
                odds -= nums[left] % 2
                left += 1

            # All subarrays ending at 'right' with start from left to right
            count += right - left + 1

        return count

    return at_most_k_odds(k) - at_most_k_odds(k - 1)


num_nice_subarrays = num_nice_subarrays_v1


def test():
    assert num_nice_subarrays(nums=[1, 1, 2, 1, 1], k=3) == 2
    assert num_nice_subarrays(nums=[2, 4, 6], k=1) == 0
    assert num_nice_subarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2) == 16
