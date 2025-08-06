from collections import deque


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


def good_nodes(root: TreeNode | None, path_max: int = 0) -> int:
    if root is None:
        return 0

    if (path_max := max(root.val, path_max)) <= root.val:
        return 1 + good_nodes(root.left, path_max) + good_nodes(root.right, path_max)
    else:
        return good_nodes(root.left, path_max) + good_nodes(root.right, path_max)


def test():
    root = make([3, 1, 4, 3, None, 1, 5])
    assert good_nodes(root) == 4

    root = make([3, 3, None, 4, 2])
    assert good_nodes(root) == 3

    root = make([2])
    assert good_nodes(root) == 1
