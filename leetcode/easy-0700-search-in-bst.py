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


def search_bst(root: TreeNode, val: int) -> TreeNode | None:
    if root.val == val:
        return root
    elif root.left and root.val < val:
        return search_bst(root.left, val)
    elif root.right and root.val > val:
        return search_bst(root.right, val)
    else:
        return None


def test():
    root = make([4, 2, 7, 1, 3])
    if node := search_bst(root, 2):
        assert node.val == 2

    root = make([4, 2, 7, 1, 3])
    if node := search_bst(root, 5):
        pass
    assert node is None


test()
