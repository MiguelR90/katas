def viz(nums: list[int]) -> list[list[int]]:
    out: list[list[int]] = []
    print(nums)
    print("-" * 50)

    def backtrack(state: list[int], start: int):
        out.append(list(state))

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                breakpoint()
                continue

            state.append(nums[i])
            print(f"{str(state):<15} start={start:<2} i={i:<2} nums[i]={nums[i]}")
            backtrack(state, i + 1)
            _ = state.pop()

    backtrack([], 0)
    print("-" * 50)
    return out


def viz2(nums: list[int]) -> list[list[int]]:
    out: list[list[int]] = []
    state: list[int] = []

    def backtrack(i: int):
        if i == len(nums):
            out.append(list(state))
            return

        # Positive case: include nums[i] then backtrack
        state.append(nums[i])
        backtrack(i + 1)
        _ = state.pop()

        # Negative case: don't include
        backtrack(i + 1)

    backtrack(0)
    return out


if __name__ == "__main__":
    import pprint

    pprint.pprint(viz([1, 1, 2, 5]))
    # pprint.pprint(viz2([1, 2, 3, 4]))
