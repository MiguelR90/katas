from typing import Literal


def play(senate: str) -> Literal["Radiant", "Dire"]:
    tumbstones: set[int] = set()

    while (
        len(winner := set(s for i, s in enumerate(senate) if i not in tumbstones)) > 1
    ):
        for i in range(len(senate)):
            if i in tumbstones:
                continue

            for j in range(len(senate)):
                if i != j and senate[i] != senate[j] and j not in tumbstones:
                    tumbstones.add(j)
                    break

    if winner.pop() == "R":
        return "Radiant"
    else:
        return "Dire"


def test():
    assert play("RD") == "Radiant"
    assert play("RDD") == "Dire"
    assert play("RDDR") == "Radiant"
    assert play("DDRRR") == "Dire"
    assert play("RRRDDDDDRRRDDDDDDDDD") == "Dire"
