"""
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.
"""


def num_alt_groups(colors: list[int], k: int) -> int:
    n = len(colors)
    groups: int = 0

    for i in range(n):
        for j in range(k - 1):
            a = (i + j) % n
            b = (i + j + 1) % n
            if colors[a] == colors[b]:
                break
        else:
            groups += 1

    return groups


def test():
    assert num_alt_groups(colors=[0, 1, 0, 1, 0], k=3) == 3
    assert num_alt_groups(colors=[0, 1, 0, 0, 1, 0, 1], k=6) == 2
    assert num_alt_groups(colors=[1, 1, 0, 1], k=4) == 0
