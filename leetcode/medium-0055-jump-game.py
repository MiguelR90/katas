"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

from collections import deque


def jumpgame_bfs(nums: list[int]) -> bool:
    queue: deque[int] = deque([0])
    seen: set[int] = set([0])

    while queue:
        current = queue.popleft()

        if current >= len(nums) - 1:
            return True

        for i in range(1, nums[current] + 1):
            if (newpos := current + i) not in seen:
                seen.add(newpos)
                queue.append(newpos)

    return False


def jumpgame_dfs(nums: list[int]) -> bool:
    memo: dict[int, bool] = {}

    def dfs(i: int) -> bool:
        if i in memo:
            return memo[i]

        if i >= len(nums) - 1:
            return memo.setdefault(i, True)

        for j in range(1, nums[i] + 1):
            if dfs(i + j):
                return memo.setdefault(i, True)

        return memo.setdefault(i, False)

    return dfs(0)


def jumpgame_greedy(nums: list[int]) -> bool:
    farthest: int = 0

    for i in range(len(nums)):
        if i > farthest:
            return False

        farthest = max(farthest, i + nums[i])

    return True


from typing import Callable
import pytest


@pytest.mark.parametrize("jumpgame", [jumpgame_bfs, jumpgame_dfs, jumpgame_greedy])
def test(jumpgame: Callable[[list[int]], bool]):
    assert jumpgame([2, 3, 1, 1, 4]) is True
    assert jumpgame([3, 2, 1, 0, 4]) is False
    assert jumpgame([0]) is True
    assert jumpgame([2, 0, 0]) is True
    assert jumpgame([2, 3, 1, 1, 4]) is True
    assert jumpgame([3, 2, 1, 0, 4]) is False
    assert jumpgame([5, 0, 0, 0, 0]) is True
    assert jumpgame([0, 2]) is False
    assert jumpgame([1, 1, 1, 1]) is True
    assert jumpgame([4, 0, 0, 0, 0, 0]) is False
    assert jumpgame([1, 0]) is True
    assert jumpgame([0, 1]) is False
