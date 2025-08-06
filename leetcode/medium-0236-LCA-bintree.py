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


def lca(root: TreeNode | None, p: int, q: int) -> int | None:
    if root is None:
        return None

    if root.val in {p, q}:
        return root.val

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root.val

    return left if left else right


def test():
    root = make([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    val = lca(root, 5, 1)
    assert val == 3

    root = make([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    val = lca(root, 5, 4)
    assert val == 5


test()
