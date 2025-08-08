def powerset(nums: list[int]) -> list[list[int]]:
    pset: list[list[int]] = []

    def dfs(i: int, state: list[int]):
        if i == len(nums):
            pset.append(state[:])
            return

        # Case1: don't include element i
        _ = dfs(i + 1, state)

        # Case2: include element i
        state.append(nums[i])
        dfs(i + 1, state)
        _ = state.pop()

    dfs(0, [])
    return pset


def permutations(nums: list[int], r: int | None = None) -> list[list[int]]:
    if r is None:
        r = len(nums)

    perms: list[list[int]] = []

    def dfs(state: list[int], seen: set[int]):
        if len(state) == r:
            perms.append(state[:])
            return

        for i in range(len(nums)):
            if i not in seen:
                _, _ = state.append(nums[i]), seen.add(i)
                dfs(state, seen)
                _, _ = state.pop(), seen.remove(i)

    dfs([], set([]))
    return perms


def combinations(nums: list[int], r: int | None = None) -> list[list[int]]:
    if r is None:
        r = len(nums)

    combs: list[list[int]] = []

    def dfs(i: int, state: list[int]):
        if len(state) == r:
            combs.append(state[:])
            return

        for j in range(i, len(nums)):
            state.append(nums[j])
            dfs(j + 1, state)
            _ = state.pop()

    dfs(0, [])
    return combs


if __name__ == "__main__":
    import pprint

    nums = list(range(4))

    pset = powerset(nums)
    pprint.pprint(pset)

    perms = permutations(nums)
    pprint.pprint(perms)

    perms = permutations(nums, 2)
    pprint.pprint(perms)

    combs = combinations(nums)
    pprint.pprint(combs)

    combs = combinations(nums, 2)
    pprint.pprint(combs)
