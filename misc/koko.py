import math


def valid(piles: list[int], speed: int, hours: int) -> bool:
    return sum(math.ceil(p / speed) for p in piles) <= hours


def search(piles: list[int], hours: int) -> int:
    if hours < len(piles):
        # need at least one hour per pile
        return -1

    def bisect(left: int, right: int) -> int:
        if left == right:
            return left

        mid = (left + right) // 2

        if valid(piles, mid, hours):
            result = bisect(left, mid)
        else:
            result = bisect(mid + 1, right)

        return result

    return bisect(math.ceil(sum(piles) / hours), max(piles))


def test_search():
    assert search([3, 6, 7, 11], 8) == 4
    assert search([30, 11, 23, 4, 20], 5) == 30
    assert search([30, 11, 23, 4, 20], 6) == 23
    assert search([1, 1, 1, 1], 4) == 1
    assert search([1000000000], 2) == 500000000

    assert search([1_000_000_000] * 10, 10) == 1_000_000_000
    assert search([1] * 100_000, 100_000) == 1


if __name__ == "__main__":
    test_search()
