import pytest

digit2letter: dict[str, str] = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

    n = len(digits)
    results: list[str] = []

    def backtracking(state: list[str], d: int):
        if d == n:
            results.append("".join(state))
            return

        digit = digits[d]
        for letter in digit2letter[digit]:
            state.append(letter)
            backtracking(state, d + 1)
            _ = state.pop()

    backtracking([], 0)
    return results


@pytest.mark.parametrize(
    "digits,expected",
    [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
        (
            "79",
            [
                "pw",
                "px",
                "py",
                "pz",
                "qw",
                "qx",
                "qy",
                "qz",
                "rw",
                "rx",
                "ry",
                "rz",
                "sw",
                "sx",
                "sy",
                "sz",
            ],
        ),
    ],
)
def test_letter_combinations(digits: str, expected: list[str]):
    result = letter_combinations(digits)
    assert sorted(result) == sorted(expected)
