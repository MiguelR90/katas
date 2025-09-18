import math
from collections import Counter
from typing import Callable


def number_dominant_1_substrings_naive(s: str) -> int:
    n = len(s)
    dominant = 0

    for i in range(n):
        freq = Counter[str]()

        for j in range(i, n):
            freq[s[j]] += 1

            if freq["0"] ** 2 <= freq["1"]:
                dominant = dominant + 1

    return dominant


def number_dominant_1_substrings_sqrt(s: str) -> int:
    n = len(s)
    sqrt_n = math.sqrt(n) + 1
    dominant = 0

    for i in range(n):
        freq = Counter[str]()

        for j in range(i, n):
            freq[s[j]] += 1

            # Early termination: if zeros > √n, no point continuing
            # because zeros² > n ≥ ones for any valid substring
            if freq["0"] > sqrt_n:
                break

            if freq["0"] ** 2 <= freq["1"]:
                dominant = dominant + 1

    return dominant


import pytest


@pytest.mark.parametrize(
    "number_dominant_1_substrings",
    [number_dominant_1_substrings_naive, number_dominant_1_substrings_sqrt],
)
def test(number_dominant_1_substrings: Callable[[str], int]):
    assert number_dominant_1_substrings("00011") == 5
    assert number_dominant_1_substrings("101101") == 16
