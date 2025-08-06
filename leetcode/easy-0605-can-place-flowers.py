from copy import copy


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    tmp_flowerbed = copy(flowerbed)

    added = 0
    for i in range(0, len(tmp_flowerbed)):
        start, end = max(0, i - 1), min(i + 1, len(tmp_flowerbed))
        if sum(tmp_flowerbed[start:end]) == 0:
            tmp_flowerbed[i] = 1
            added += 1

    return n <= added


def test():
    assert can_place_flowers([1, 0, 0, 0, 1], 1)
    assert not can_place_flowers([1, 0, 0, 0, 1], 2)
    assert can_place_flowers([1, 0, 0, 0, 1, 0, 0], 2)
