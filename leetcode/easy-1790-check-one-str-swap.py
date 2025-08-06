def check(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    i: int = 0
    while i < len(s1) and s1[i] == s2[i]:
        i += 1

    l1: list[str] = list(s1)
    for j in range(i + 1, len(l1)):
        if l1[j] == s2[i]:
            l1[i], l1[j] = l1[j], l1[i]

    return "".join(l1) == s2


def test():
    assert check("bank", "kanb") is True
    assert check("attck", "defend") is False
    assert check("kelb", "kelb") is True


test()
