def climb(n: int) -> int:
    if n < 3:
        return n

    prev, current = 1, 2
    for i in range(3, n + 1):
        prev, current = current, current + prev

    return current


def test():
    assert climb(1) == 1
    assert climb(2) == 2
    assert climb(3) == 3
    assert climb(4) == 5
    assert climb(5) == 8
    assert climb(10) == 89


if __name__ == "__main__":
    test()

"""
1

1

1, 1
2

1, 1, 1
2, 1
1, 2

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

1, 1, 1, 1, 1
2, 1, 1, 1
1, 2, 1, 1
1, 1, 2, 1
2, 2, 1
1, 1, 1, 2
2, 1, 2
1, 2, 2
"""
