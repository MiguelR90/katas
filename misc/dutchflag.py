import copy
from typing import Callable


def dutchflag_nestedloop(nums: list[int], pivot_index: int) -> list[int]:
    n = len(nums)
    pivot = nums[pivot_index]

    for i in range(n):
        if nums[i] < pivot:
            continue

        for j in range(i + 1, n):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                break

    for i in reversed(range(n)):
        if nums[i] > pivot:
            continue

        for j in reversed(range(i - 1)):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                break

    return nums


def dutchflag_singleloop(nums: list[int], pivot_index: int) -> list[int]:
    n = len(nums)
    pivot = nums[pivot_index]

    smaller: int = 0
    for i in range(n):
        if nums[i] < pivot:
            nums[smaller], nums[i] = nums[i], nums[smaller]
            smaller += 1

    larger: int = n - 1
    for i in reversed(range(n)):
        if nums[i] < pivot:
            break
        elif pivot < nums[i]:
            nums[i], nums[larger] = nums[larger], nums[i]
            larger -= 1

    return nums


def dutchflag_while(nums: list[int], pivot_index: int) -> list[int]:
    pivot = nums[pivot_index]

    smaller, equal, larger = 0, 0, len(nums)

    while equal < larger:
        if nums[equal] < pivot:
            nums[equal], nums[smaller] = nums[smaller], nums[equal]
            smaller += 1
            equal += 1
        elif nums[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            nums[equal], nums[larger] = nums[larger], nums[equal]

    return nums


def main(dutchflag: Callable[[list[int], int], list[int]]):
    nums: list[int] = [0, 1, 2, 0, 2, 1, 1]
    import pprint

    pprint.pprint(dutchflag(copy.copy(nums), 0))
    pprint.pprint(dutchflag(copy.copy(nums), 1))
    pprint.pprint(dutchflag(copy.copy(nums), 2))


for dutchflag in [dutchflag_nestedloop, dutchflag_singleloop, dutchflag_while]:
    print()
    main(dutchflag)
