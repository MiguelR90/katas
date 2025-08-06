def combsum(nums: list[int], target: int) -> list[list[int]]:
    out: list[list[int]] = []
    nums = sorted(nums)

    def backtrack(state: list[int], start: int = 0, current_sum: int = 0):
        if current_sum == target:
            out.append(list(state))
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            if (new_sum := current_sum + nums[i]) <= target:
                state.append(nums[i])
                backtrack(state, i + 1, new_sum)
                _ = state.pop()

    backtrack([])
    return out


if __name__ == "__main__":
    import pprint

    pprint.pprint(combsum([1, 1, 2, 5, 6, 7, 10], 8))
