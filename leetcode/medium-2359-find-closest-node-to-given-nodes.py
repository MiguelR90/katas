def compute_distances(edges: list[int], node: int) -> list[int]:
    distances: list[int] = [-1] * len(edges)
    d: int = 0
    n: int = node
    while n != -1:
        distances[n] = d
        n = edges[n]
        d += 1

    return distances


def find_closest(edges: list[int], node1: int, node2: int) -> int:
    # improve by checking conidtions early
    dist1: list[int] = compute_distances(edges, node1)
    dist2: list[int] = compute_distances(edges, node2)

    closest: int = -1
    min_dist: int = len(edges)  # largest posible distance
    for node, (d1, d2) in enumerate(zip(dist1, dist2)):
        if d1 >= 0 and d2 >= 0 and (d := max(d1, d2)) < min_dist:
            closest = node
            min_dist = d

    return closest


def test():
    # assert find_closest([2, 2, 3, -1], 0, 1) == 2
    assert find_closest([1, 2, -1], 0, 2) == 2


test()
