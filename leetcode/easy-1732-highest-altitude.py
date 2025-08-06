from itertools import accumulate
import operator


def highest_altitude(gain: list[int]) -> int:
    # alt: Iterable[int] = accumulate(gain, func=operator.add, initial=0)
    # return max(alt)
    return max(accumulate(gain, func=operator.add, initial=0))


# without using the special accumlate function
def highest_altitude2(gain: list[int]) -> int:
    current_alt, max_alt = 0, 0
    for delta in gain:
        if max_alt < (current_alt := current_alt + delta):
            max_alt = current_alt

    return max_alt


def test():
    assert highest_altitude([-5, 1, 5, 0, -7]) == 1
    assert highest_altitude2([-5, 1, 5, 0, -7]) == 1

    assert highest_altitude([-4, -3, -2, -1, 4, 3, 2]) == 0
    assert highest_altitude2([-4, -3, -2, -1, 4, 3, 2]) == 0
