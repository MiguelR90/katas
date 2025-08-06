def sum_candidates(candidate: list[int], target: int) -> list[list[int]]:
    out: list[list[int]] = []
    observed: set[tuple[int, ...]] = set()
    candidate = sorted(candidate)

    def backtracking(state: list[int], current_sum: int, start_idx: int):
        key = tuple(state)
        if current_sum == target and key not in observed:
            observed.add(key)
            out.append(list(state))
            return

        for i in range(start_idx, len(candidate)):
            c = candidate[i]
            if current_sum + c <= target:
                state.append(c)
                backtracking(state, current_sum + c, i)  # allow reuse
                state.pop()
            else:
                break

    backtracking([], 0, 0)
    return out


def test():
    import pprint

    pprint.pprint(sum_candidates([7, 3, 6, 2], 7))


if __name__ == "__main__":
    test()
