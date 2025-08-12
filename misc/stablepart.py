def stable_partition(nums: list[int], pivot: int) -> int:
    i, j = 0, 0

    while j < len(nums):
        if nums[j] < pivot:
            # NOTE: sliding j all the way to i makes the algorithm O(n^2)
            k = j
            while i < k:
                nums[k - 1], nums[k] = nums[k], nums[k - 1]
                k -= 1

            i += 1

        j += 1

    return i


def test_stable_partition():
    nums = [3, 1, 4, 2, 5]
    assert stable_partition(nums, 3) == 2
    assert nums == [1, 2, 3, 4, 5]

    nums = [1, 2, 3, 4, 5]
    assert stable_partition(nums, 3) == 2
    assert nums == [1, 2, 3, 4, 5]

    nums = [5, 4, 3, 2, 1]
    assert stable_partition(nums, 3) == 2
    assert nums == [2, 1, 5, 4, 3]

    nums = [3, 3, 3]
    assert stable_partition(nums, 3) == 0
    assert nums == [3, 3, 3]

    nums = [1, 1, 1]
    assert stable_partition(nums, 3) == 3
    assert nums == [1, 1, 1]
