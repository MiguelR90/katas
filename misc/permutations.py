import copy


def permutations(n: int) -> list[list[int]]:
    perms: list[list[int]] = []

    def backtrack(state: list[int], perms: list[list[int]]):
        if len(state) == n:
            perms.append(copy.copy(state))

        for i in range(1, n + 1):
            if i not in state:
                state.append(i)
                backtrack(state, perms)
                state.remove(i)

    backtrack([], perms)

    return perms


if __name__ == "__main__":
    import math
    import pprint

    perms = permutations(4)
    assert len(set("".join(map(str, x)) for x in perms)) == math.factorial(4)

    pprint.pprint(perms)
