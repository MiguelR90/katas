from collections import deque
from copy import deepcopy, copy


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


def path_sum(root: TreeNode | None, target_sum: int, current_sum: int = 0) -> int:
    if root is None:
        return 0

    if (current_sum := current_sum + root.val) == target_sum:
        return (
            1
            + path_sum(root.left, target_sum, 0)
            + path_sum(root.left, target_sum, current_sum)
            + path_sum(root.right, target_sum, 0)
            + path_sum(root.right, target_sum, current_sum)
        )
    else:
        return (
            path_sum(root.left, target_sum, 0)
            + path_sum(root.left, target_sum, current_sum)
            + path_sum(root.right, target_sum, 0)
            + path_sum(root.right, target_sum, current_sum)
        )


def test():
    root = make([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    assert path_sum(root, 8) == 3

    root = make([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    assert path_sum(root, 22) == 3


test()
