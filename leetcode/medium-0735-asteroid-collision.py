from typing import Literal


def sign(num: int) -> Literal[1, -1]:
    if num >= 0:
        return 1
    else:
        return -1


def asteroid_collision(asteroids: list[int]) -> list[int]:
    backlog: list[int] = []

    for ast in asteroids:
        if not backlog or sign(backlog[-1]) == sign(ast):
            backlog.append(ast)
        elif abs(backlog[-1]) == abs(ast):
            _ = backlog.pop()
        elif abs(backlog[-1]) > abs(ast):
            pass
        elif abs(backlog[-1]) < abs(ast):
            while backlog and abs(backlog[-1]) < abs(ast):
                _ = backlog.pop()
            if not backlog:
                backlog.append(ast)

    return backlog


def asteroid_collision2(asteroids: list[int]) -> list[int]:
    backlog: list[int] = []

    i: int = 0
    while i < len(asteroids):
        ast: int = asteroids[i]

        if not backlog or sign(backlog[-1]) == sign(ast):
            backlog.append(ast)
            i += 1
        elif abs(backlog[-1]) == abs(ast):
            _ = backlog.pop()
            i += 1
        elif abs(backlog[-1]) > abs(ast):
            i += 1
        elif abs(backlog[-1]) < abs(ast):
            _ = backlog.pop()

    return backlog


def test():
    assert asteroid_collision2([5, 10, -5]) == [5, 10]
    assert asteroid_collision2([8, -8]) == []
    assert asteroid_collision2([10, 2, -5]) == [10]
    assert asteroid_collision2([14, -6, 9, -7, -9, -20, -14, 5, 9, -2]) == [
        -20,
        -14,
        -2,
    ]
