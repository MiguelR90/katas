def max_water(height: list[int]) -> int:
    volumn: int = 0
    for x1, y1 in enumerate(height[:-1]):
        for x2, y2 in enumerate(height[x1:], start=x1):
            if volumn < (v := (x2 - x1) * min(y1, y2)):
                volumn = v

    return volumn


def test():
    assert max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
