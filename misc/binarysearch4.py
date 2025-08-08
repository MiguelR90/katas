from collections.abc import Callable
import pytest


def search_iteration(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def search_recursion(nums: list[int], target: int):
    def bs(left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return bs(left, mid - 1)
        else:
            return bs(mid + 1, right)

    return bs(0, len(nums) - 1)


@pytest.mark.parametrize("search", [search_iteration, search_recursion])
def test_search(search: Callable[[list[int], int], int]):
    assert search([1, 2, 3, 4, 5], 4) == 3
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([], 1) == -1
    assert search([1], 1) == 0
    assert search([1], 0) == -1
