from collections import deque
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


def zig_zag(
    root: TreeNode | None, direction: Literal["left", "right"] | None = None
) -> int:
    if root is None:
        return 0

    if direction and direction == "left":
        return max(zig_zag(root.left, "left"), 1 + zig_zag(root.right, "right"))

    elif direction and direction == "right":
        return max(1 + zig_zag(root.left, "left"), zig_zag(root.right, "right"))

    elif direction is None:
        return max(zig_zag(root.left, "left"), zig_zag(root.right, "right"))


def test():
    root = make([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1])
    assert zig_zag(root) == 3
    root = make([1, 1, 1, None, 1, None, None, 1, 1, None, 1])
    assert zig_zag(root) == 4


test()
