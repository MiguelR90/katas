from collections import deque


def schedule(
    num_courses: int, prerequisits: list[list[int]], queries: list[list[int]]
) -> list[bool]:
    def path(source: int, sink: int) -> bool:
        q: deque[int] = deque([source])

        while q:
            current: int = q.popleft()
            for a, b in ((a, b) for a, b in prerequisits if a == current):
                if b == sink:
                    return True

                q.append(b)

        return False

    return [path(a, b) for a, b in queries]


def test():
    assert schedule(2, [[1, 0]], [[0, 1], [1, 0]]) == [False, True]
    assert schedule(2, [], [[1, 0], [0, 1]]) == [False, False]
    assert schedule(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]) == [True, True]


test()
