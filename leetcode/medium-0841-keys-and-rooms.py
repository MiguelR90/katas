def can_visit(rooms: list[list[int]]) -> bool:
    to_visit: list[int] = [0]
    visited: set[int] = set()

    while to_visit and len(visited) < len(rooms):
        if (room := to_visit.pop()) not in visited:
            visited.add(room)
            to_visit.extend(rooms[room])

    return len(visited) == len(rooms)


def test():
    assert can_visit([[1], [2], [3], []]) is True
    assert can_visit([[1, 3], [3, 0, 1], [2], [0]]) is False


test()
