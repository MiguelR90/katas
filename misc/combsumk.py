def combsum(k: int, n: int) -> list[list[int]]:
    nums: list[int] = list(range(1, 10))
    out: list[list[int]] = []
    state: list[int] = []

    def backtrack(start: int, current_sum: int):
        if len(state) == k and current_sum == n:
            out.append(list(state))
            return

        for i in range(start, len(nums)):
            if current_sum + nums[i] <= n:
                state.append(nums[i])
                backtrack(i + 1, current_sum + nums[i])
                _ = state.pop()

    backtrack(0, 0)
    return out


if __name__ == "__main__":
    import pprint

    pprint.pprint(combsum(3, 7))
    pprint.pprint(combsum(3, 9))
