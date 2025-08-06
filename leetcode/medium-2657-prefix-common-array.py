def prefix(a: list[int], b: list[int]) -> list[int]:
    out: list[int] = []
    set_a: set[int] = set()
    set_b: set[int] = set()

    for aa, bb in zip(a, b):
        set_a.add(aa)
        set_b.add(bb)
        out.append(len(set_a.intersection(set_b)))

    return out


def test():
    assert prefix([1, 3, 2, 4], [3, 1, 2, 4]) == [0, 2, 3, 4]
    assert prefix([2, 3, 1], [3, 1, 2]) == [0, 1, 3]


test()
