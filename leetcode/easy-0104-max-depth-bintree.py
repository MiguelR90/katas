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


def max_depth(root: TreeNode | None) -> int:
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


# balanced tree: ceil(log2(n+1)) <= height <= n
# therefore max depth ~= ceil(log2(n+1))


def test():
    input = [3, 9, 20, None, None, 15, 7]
    tree = make(input)
    treelist = to_list(tree)
    assert treelist == list(i for i in input if i is not None)
    assert max_depth(tree) == 3

    input = list(range(100))
    tree = make(input)
    treelist = to_list(tree)
    assert treelist == list(i for i in input if i is not None)
    assert max_depth(tree) == 7

    input = [3]
    tree = make(input)
    treelist = to_list(tree)
    assert treelist == list(i for i in input if i is not None)
    assert max_depth(tree) == 1

    input = [3, 2]
    tree = make(input)
    treelist = to_list(tree)
    assert treelist == list(i for i in input if i is not None)
    assert max_depth(tree) == 2
