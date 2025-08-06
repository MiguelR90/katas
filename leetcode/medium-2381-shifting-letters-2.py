from itertools import zip_longest
import string


letters = list(string.ascii_lowercase)
forwards = dict(zip_longest(letters, letters[1:], fillvalue=letters[0]))
backward = dict(zip_longest(letters[::-1], letters[:-1][::-1], fillvalue=letters[-1]))


def shift_letters(s: str, shifts: list[list[int]]) -> str:
    for left, right, direction in shifts:
        subs: list[str] = []
        for c in s[left : right + 1]:
            if direction == 0:
                subs.append(backward[c])
            else:
                subs.append(forwards[c])

        s = s[:left] + "".join(subs) + s[right + 1 :]
    return s


def test():
    assert shift_letters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace"
    assert shift_letters("dztz", [[0, 0, 0], [1, 1, 1]]) == "catz"


test()
