def num_subarray_sizek_gt_threshold(nums: list[int], k: int, threshold: int) -> int:
    cursum: int = sum(nums[:k])
    count: int = int(cursum / k >= threshold)

    for i in range(k, len(nums)):
        cursum -= nums[i - k]
        cursum += nums[i]

        if cursum / k >= threshold:
            count += 1

    return count


def test():
    assert num_subarray_sizek_gt_threshold([2, 2, 2, 2, 5, 5, 5, 8], 3, 4) == 3
    assert (
        num_subarray_sizek_gt_threshold([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5) == 6
    )


if __name__ == "__main__":
    num_subarray_sizek_gt_threshold([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
    num_subarray_sizek_gt_threshold([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5)
