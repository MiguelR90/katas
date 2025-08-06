from collections import deque
from itertools import zip_longest
from typing import Literal


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


def make(values: list[int | None] | list[int]) -> TreeNode:
    if not values or values[0] is None:
        raise RuntimeError

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while i < len(values):
        current = queue.popleft()

        # check i < len(values) is redundant
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


def right_side(root: TreeNode | None) -> list[int]:
    if root is None:
        return []

    right = right_side(root.right)
    left = right_side(root.left)
    out: list[int] = [root.val]
    for r, l in zip_longest(right, left):
        if r:
            out.append(r)
        else:
            out.append(l)

    return out


def test():
    root = make([1, 2, 3, None, 5, None, 4])
    assert right_side(root) == [1, 3, 4]

    root = make([1, 2, 3, 4, None, None, None, 5])
    assert right_side(root) == [1, 3, 4, 5]


test()
