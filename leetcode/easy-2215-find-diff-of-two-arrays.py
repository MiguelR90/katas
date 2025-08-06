def find_diff_off_arrays(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    answer: list[list[int]] = []
    answer.append(list(set(nums1).difference(nums2)))
    answer.append(list(set(nums2).difference(nums1)))
    return answer


def test():
    out = find_diff_off_arrays([1, 2, 3], [2, 4, 6])
    assert set(out[0]) == set([1, 3])
    assert set(out[1]) == set([4, 6])

    out = find_diff_off_arrays([1, 2, 3, 3], [1, 1, 2, 2])
    assert set(out[0]) == set([3])
    assert set(out[1]) == set([])
