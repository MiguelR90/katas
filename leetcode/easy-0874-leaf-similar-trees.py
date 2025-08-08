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


def to_list(node: TreeNode) -> list[int]:
    output: list[int] = []
    queue: deque[TreeNode] = deque([node])

    while queue:
        current = queue.popleft()
        output.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return output


# this needs to be depth first search instead of breadth
def leaf_value_sequence(root: TreeNode | None) -> list[int]:
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [root.val]

    output: list[int] = []
    output.extend(leaf_value_sequence(root.left))
    output.extend(leaf_value_sequence(root.right))
    return output


def leaf_similar(root1: TreeNode, root2: TreeNode) -> bool:
    return leaf_value_sequence(root1) == leaf_value_sequence(root2)


def test():
    root1 = make([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
    root2 = make([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
    assert leaf_similar(root1, root2) is True

    root1 = make([1, 2, 3])
    root2 = make([1, 3, 2])
    assert leaf_similar(root1, root2) is False
