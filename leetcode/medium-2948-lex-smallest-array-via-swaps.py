def lex_array(nums: list[int], limit: int) -> list[int]:
    for i, a in enumerate(nums[:-1]):
        if candidates := [
            (j, b)
            for j, b in enumerate(nums[i + 1 :], i + 1)
            if b < a and abs(a - b) <= limit
        ]:
            j, _ = min(candidates, key=lambda x: x[1])
            nums[i], nums[j] = nums[j], nums[i]

    return nums


def test():
    assert lex_array([1, 5, 3, 9, 8], 2) == [1, 3, 5, 8, 9]
    assert lex_array([1, 7, 6, 18, 2, 1], 3) == [1, 6, 7, 18, 1, 2]
    assert lex_array([1, 7, 28, 19, 10], 3) == [1, 7, 28, 19, 10]


test()
