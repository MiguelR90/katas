from collections import deque


def reorder(edges: list[list[int]]) -> int:
    swaps: int = 0
    has_path: set[int] = set([0])
    queue: deque[list[int]] = deque(edges)

    while queue:
        source, sink = queue.popleft()
        if sink in has_path:
            has_path.add(source)
        elif source in has_path:
            swaps += 1
            has_path.add(sink)
        else:
            queue.append([source, sink])

    return swaps


def test():
    assert reorder([[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
    assert reorder([[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    assert reorder([[1, 0], [2, 0]]) == 0


test()
