import sys

sys.setrecursionlimit(10000)


def coin_change_top_down(coins: list[int], target: int) -> int:
    memo: dict[int, int] = {0: 0}

    def dp(target: int) -> int:
        if target < 0:
            return -1
        if target in memo:
            return memo[target]

        subproblems: list[int] = []
        for c in coins:
            if (result := dp(target - c)) != -1:
                subproblems.append(result)

        if not subproblems:
            memo[target] = -1
        else:
            memo[target] = 1 + min(subproblems)

        return memo[target]

    return dp(target)


def coin_change_bottom_up(coins: list[int], target: int) -> int:
    table: list[int | None] = [None] * (target + 1)

    table[0] = 0
    for c in (c for c in coins if c <= target):
        table[c] = 1

    for i in range(1, target + 1):
        if table[i] is None:
            subp = [table[i - c] for c in coins if i - c >= 0 and table[i - c] != -1]

            if not subp:
                table[i] = -1
            else:
                table[i] = 1 + min(subp)

    return table[-1]


# coin_change = coin_change_top_down
coin_change = coin_change_bottom_up


def test_coin_change():
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert coin_change([2], 3) == -1  # Cannot make 3 with only 2s
    assert coin_change([1], 0) == 0  # No coins needed
    assert coin_change([1], 2) == 2  # 1 + 1
    assert coin_change([186, 419, 83, 408], 6249) == 20  # Stress test
    assert coin_change([3, 7, 405, 436], 8839) == 25  # Stress test with large coins


if __name__ == "__main__":
    test_coin_change()
