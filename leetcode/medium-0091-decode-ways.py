# leetcode/medium-0091-decode-ways.py


mapping: dict[str, str] = {str(i): chr(64 + i) for i in range(1, 27)}


def decode_topdown(s: str) -> int:
    n = len(s)

    def dp(i: int) -> int:
        if i == n:
            return 1

        paths: int = 0
        if s[i] in mapping:
            paths += dp(i + 1)

        if i + 2 <= n and s[i : i + 2] in mapping:
            paths += dp(i + 2)

        return paths

    return dp(0)


from typing import Callable
import pytest


@pytest.mark.parametrize("decode", [decode_topdown])
def test(decode: Callable[[str], int]):
    assert decode("12") == 2
    assert decode("226") == 3
    assert decode("06") == 0
