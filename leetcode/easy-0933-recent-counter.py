from itertools import takewhile


class RecentCounter:
    def __init__(self) -> None:
        self._requests: list[int] = []

    def ping(self, req: int) -> int:
        self._requests.append(req)
        return sum(
            1 for _ in takewhile(lambda r: req - 3000 <= r, reversed(self._requests))
        )


def test():
    c = RecentCounter()
    assert c.ping(1) == 1
    assert c.ping(100) == 2
    assert c.ping(3001) == 3
    assert c.ping(3002) == 3
