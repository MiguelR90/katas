from typing import Callable
import copy
import pprint


def dutchflag(nums: list[int], pivot_index: int) -> list[int]:
    pivot = nums[pivot_index]

    # This is the invariant which we will follow:
    # nums[:smaller] -> nums[i] < pivot
    # nums[smaller:equal] -> nums[i] == pivot
    # nums[equal:larger] -> nums[i] which remain unclassified
    # nums[larger:] -> nums[i] > pivot

    smaller, equal, larger = 0, 0, len(nums)

    while equal < larger:
        if nums[equal] < pivot:
            nums[smaller], nums[equal] = nums[equal], nums[smaller]
            smaller += 1
            equal += 1
        elif nums[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            nums[larger], nums[equal] = nums[equal], nums[larger]

    return nums


def test_dutchflag():
    nums = [1, 2, 3, 3, 2, 1, 1, 2, 3, 4, 5, 0, 0]
    pprint.pprint(dutchflag(copy.copy(nums), 0))
    pprint.pprint(dutchflag(copy.copy(nums), 1))
    pprint.pprint(dutchflag(copy.copy(nums), 2))


test_dutchflag()


def condpart(nums: list[int], cond: Callable[[int], bool]) -> list[int]:
    # INVARIANT:
    # nums[:pivot] -> cond(nums[i]) -> False
    # nums[pivot:i] -> cond(nums[i]) -> True
    # nums[i:] -> unclassified

    pivot: int = 0

    for i in range(len(nums)):
        if not cond(nums[i]):
            nums[pivot], nums[i] = nums[i], nums[pivot]
            pivot += 1

    return nums


def test_condpart():
    nums = [1, 2, 3, 3, 2, 1, 1, 2, 3, 4, 5, 0, 0]
    pprint.pprint(condpart(copy.copy(nums), lambda x: x == 1))
    pprint.pprint(condpart(copy.copy(nums), lambda x: x == 2))
    pprint.pprint(condpart(copy.copy(nums), lambda x: x == 3))


print()
test_condpart()
