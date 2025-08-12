from itertools import filterfalse
import math


def powerset(nums: list[int]) -> list[list[int]]:
    results: list[list[int]] = []

    def dfs(i: int, state: list[int]):
        if i == len(nums):
            results.append(state[:])
            return

        dfs(i + 1, state)

        state.append(nums[i])
        dfs(i + 1, state)
        _ = state.pop()

    dfs(0, [])
    return results


def combinations(nums: list[int], r: int) -> list[list[int]]:
    results: list[list[int]] = []

    def dfs(i: int, state: list[int]):
        if len(state) == r:
            results.append(state[:])
            return

        for j in range(i, len(nums)):
            state.append(nums[j])
            dfs(j + 1, state)
            _ = state.pop()

        return

    dfs(0, [])
    return results


def permutations(nums: list[int], r: int) -> list[list[int]]:
    results: list[list[int]] = []

    def dfs(state: list[int], seen: set[int]):
        if len(state) == r:
            results.append(state[:])
            return

        for i in filterfalse(lambda i: i in seen, range(len(nums))):
            _, _ = state.append(nums[i]), seen.add(i)
            dfs(state, seen)
            _, _ = state.pop(), seen.remove(i)

    dfs([], set())
    return results


def test():
    nums: list[int] = [1, 2, 3, 4]
    assert len(powerset(nums)) == 2 ** len(nums)

    r: int = 2
    assert len(combinations(nums, r)) == math.comb(len(nums), r)
    assert len(permutations(nums, r)) == math.perm(len(nums), r)


if __name__ == "__main__":
    import pprint

    nums: list[int] = [1, 2, 3, 4]
    pprint.pprint(powerset(nums))
    print()
    pprint.pprint(combinations(nums, 2))
    print()
    pprint.pprint(permutations(nums, 2))
