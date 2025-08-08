import pprint
import copy
from typing import Iterable


def permutations(n: int) -> list[list[int]]:
    perms: list[list[int]] = []

    def backtracking(state: list[int]):
        if len(state) == n:
            perms.append(copy.copy(state))
            return

        for i in range(1, n + 1):
            if i in state:
                continue

            state.append(i)
            backtracking(state)
            state.remove(i)

    backtracking([])

    return perms


def generate_perms(n: int, state: list[int] | None = None) -> Iterable[list[int]]:
    if state is None:
        state = []

    if len(state) == n:
        yield copy.copy(state)

    for i in filter(lambda i: i not in state, range(1, n + 1)):
        state.append(i)
        yield from generate_perms(n, state)
        state.remove(i)


def test():
    pprint.pprint(permutations(4))
    print("here is wehre we rand the iterator")
    pprint.pprint(list(generate_perms(4)))


if __name__ == "__main__":
    test()
