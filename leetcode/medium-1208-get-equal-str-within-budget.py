def compute_ascii_distance(a: str, b: str) -> int:
    return abs(ord(a) - ord(b))


def num_eq_substr(s: str, t: str, maxcost: int) -> int:
    longest: int = 0
    left: int = 0
    cost: int = 0

    for right in range(len(s)):
        cost += compute_ascii_distance(s[right], t[right])

        while cost > maxcost:
            cost -= compute_ascii_distance(s[left], t[left])
            left += 1

        longest = max(longest, right - left + 1)

    return longest


def test():
    assert num_eq_substr(s="abcd", t="bcdf", maxcost=3) == 3
    assert num_eq_substr(s="abcd", t="cdef", maxcost=3) == 1
    assert num_eq_substr(s="abcd", t="acde", maxcost=0) == 1
