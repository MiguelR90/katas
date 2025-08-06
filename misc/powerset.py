def powerset(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)  # okay to copy
    out: list[list[int]] = []

    def backtrack(state: list[int], start: int):
        out.append(list(state))

        for i in range(start, len(nums)):
            num = nums[i]
            if i > start and num == nums[i - 1]:
                continue

            state.append(num)
            backtrack(state, i + 1)
            _ = state.pop()

    backtrack([], 0)
    return out


def test():
    import pprint

    pprint.pprint(powerset([1, 4, 2, 2]))


if __name__ == "__main__":
    test()
