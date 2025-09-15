from collections import deque


def contains_nearby_almost_dupicate(
    nums: list[int], index_diff: int, value_diff: int
) -> bool:
    left = 0
    window: deque[int] = deque()

    for right in range(len(nums)):
        while right - left > index_diff:
            _ = window.popleft()
            left += 1

        if any(abs(nums[right] - x) <= value_diff for x in window):
            return True

        window.append(nums[right])

    return False


def test_solution():
    assert contains_nearby_almost_dupicate([1, 2, 3, 1], 3, 0) is True
    assert contains_nearby_almost_dupicate([1, 5, 9, 1, 5, 9], 2, 3) is False
    assert contains_nearby_almost_dupicate([1, 3, 6, 2], 1, 2) is True
    assert contains_nearby_almost_dupicate([1, 2], 0, 1) is False

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
