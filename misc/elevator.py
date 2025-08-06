"""
// ElevatorA
// At floor 2, going to 7
// ElevatorB
// At floor 5, going to 2
// User: on floor 4, press up

// ElevatorA
// At floor 2, going to 9
// ElevatorB
// At floor 4, going to 6
// User: on floor 1, press up

"""

import dataclasses
from typing import Literal


@dataclasses.dataclass
class Elevator:
    id: str
    floor: int
    going_to: int
    distance: int = 10**9


def sign(value: int) -> Literal[-1, 1]:
    if value < 0:
        return -1
    else:
        return 1


def pickup(elevators: list[Elevator], user: int, dir: int) -> str:
    for e in elevators:
        if (
            sign(e.going_to - e.floor) == sign(user - e.floor)
            and sign(e.going_to - e.floor) == dir
        ):
            e.distance = abs(user - e.floor)
        else:
            e.distance = abs(e.going_to - e.floor) + abs(e.going_to - user)

    r = min(elevators, key=lambda e: e.distance)

    return r.id


def test():
    assert pickup([Elevator("A", 2, 7), Elevator("B", 5, 2)], 4, 1) == "A"
    assert pickup([Elevator("A", 2, 9), Elevator("B", 4, 6)], 1, 1) == "B"


test()
