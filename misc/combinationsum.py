import pytest


def combination_sum(nums: list[int], target: int) -> list[list[int]]:
    results: list[list[int]] = []

    def backtrack(state: list[int], current_sum: int, current_index: int):
        if current_sum == target:
            results.append(state[:])
            return

        for i in range(current_index, len(nums)):
            if (new_sum := current_sum + nums[i]) <= target:
                state.append(nums[i])
                backtrack(state, new_sum, i)
                _ = state.pop()

    backtrack([], 0, 0)
    return results


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
        ([1], 2, [[1, 1]]),
        ([1], 1, [[1]]),
    ],
)
def test_combination_sum(nums: list[int], target: int, expected: list[list[int]]):
    result = combination_sum(nums, target)

    # Convert to sorted tuples to check ignoring order
    assert sorted([tuple(sorted(comb)) for comb in result]) == sorted(
        [tuple(sorted(comb)) for comb in expected]
    )

    # Check each sum matches target
    for comb in result:
        assert sum(comb) == target

    # Check only valid results are used
    for comb in result:
        assert all(c in nums for c in comb)
