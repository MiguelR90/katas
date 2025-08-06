def num_of_provinces(is_connected: list[list[int]]) -> int:
    visited: set[int] = set()
    provinces: int = 0
    for i in range(len(is_connected)):
        if i not in visited:
            provinces += 1
            visited.add(i)

        for j, connected in enumerate(is_connected[i]):
            if i != j and connected == 1:
                visited.add(j)

    return provinces


def test():
    assert num_of_provinces([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert num_of_provinces([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3


test()
