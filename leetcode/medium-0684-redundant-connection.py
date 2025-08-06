from collections import deque


# this is not correct because it used bfs
def redundant_bfs(edges: list[list[int]]) -> list[int] | None:
    start: int = edges[0][0]
    queue: deque[int] = deque([start])
    connected: set[int] = set([start])

    while queue:
        current = queue.popleft()
        for i, j in ((i, j) for i, j in edges if i == current):
            # j is already in the connected component -> cycle!
            if j in connected:
                return [i, j]

            connected.add(j)
            queue.append(j)

    return None


def redundant(edges: list[list[int]]) -> list[int] | None:
    connected: set[int] = set()

    for i, j in edges:
        if i not in connected and j not in connected:
            connected.update([i, j])
        elif i not in connected:
            connected.add(i)
        elif j not in connected:
            connected.add(j)
        else:
            return [i, j]

    return None


def test():
    assert redundant([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert redundant([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]


test()
