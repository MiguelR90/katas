from typing import Final


DECODE_MAP: Final = {str(i): chr(64 + i) for i in range(1, 27)}
MAX_STR: Final = max(len(k) for k in DECODE_MAP.keys())


def num_decodings_backtracking(s: str) -> int:
    def backtracking(state: int, curr_count: int):
        if state > len(s):
            return curr_count
        elif state == len(s):
            curr_count += 1
            return curr_count

        for di in range(1, MAX_STR + 1):
            i, j = state, state + di
            if s[i:j] in DECODE_MAP:
                state = j
                curr_count = backtracking(state, curr_count)
                state = i

        return curr_count

    return backtracking(0, 0)


def num_decodings_bottom_up(s: str) -> int:
    table_counts: list[int] = [0] * (len(s) + 1)
    table_counts[0] = 1

    if s[:1] in DECODE_MAP:
        table_counts[1] = 1

    for i in range(2, len(table_counts)):
        current = 0
        if s[i - 2 : i] in DECODE_MAP:
            current += table_counts[i - 2]

        if s[i - 1 : i] in DECODE_MAP:
            current += table_counts[i - 1]

        table_counts[i] = current

    return table_counts[-1]


def num_decodings_top_down(s: str) -> int:
    if not s:
        return 0

    memo: dict[int, int] = {0: 1}

    def dp(i: int) -> int:
        if i in memo:
            return memo[i]

        counts = 0
        if s[i - 2 : i] in DECODE_MAP:
            counts += dp(i - 2)
        if s[i - 1 : i] in DECODE_MAP:
            counts += dp(i - 1)

        memo[i] = counts
        return memo[i]

    return dp(len(s))


# num_decodings = num_decodings_backtracking
# num_decodings = num_decodings_bottom_up
num_decodings = num_decodings_top_down


def test_num_decodings():
    assert num_decodings("12") == 2  # "AB" (1 2) or "L" (12)
    assert num_decodings("226") == 3  # "BZ" (2 26), "VF" (22 6), "BBF" (2 2 6)
    assert num_decodings("06") == 0  # Invalid, can't start with '0'
    assert num_decodings("10") == 1  # "J" (10)
    assert num_decodings("2101") == 1  # "U", "A"
    assert num_decodings("11106") == 2  # "AAJF" and "KJF"
    assert num_decodings("0") == 0  # Invalid
    assert num_decodings("27") == 1  # Only "BG", not "AA" (27 > 26)
    assert num_decodings("2611055971756562") == 4  # Stress test
