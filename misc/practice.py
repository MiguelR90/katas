input = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
output = [i for i in input if i % 2 == 0]
assert output == [4, 16, 36, 64, 100]


def max_of_three(a: int, b: int, c: int) -> int:
    maximum = a

    if maximum < b:
        maximum = b

    if maximum < c:
        maximum = c

    return maximum


assert max_of_three(3, 1, 2) == 3
assert max_of_three(1, 4, 1) == 4
assert max_of_three(1, 3, 9) == 9


def max(*args: int) -> int:
    maximum = args[0]

    for a in args[1:]:
        if maximum < a:
            maximum = a

    return maximum


assert max(3, 1, 2) == 3
assert max(1, 4, 1) == 4
assert max(1, 3, 9) == 9


import re


def count_hi(s: str) -> int:
    return sum(1 for _ in re.finditer("hi", s))


def test():
    assert count_hi("hi") == 1
