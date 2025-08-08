from collections import defaultdict, deque


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


def max_level_sum(root: TreeNode) -> int:
    queue: deque[tuple[int, TreeNode]] = deque([(1, root)])

    levels: defaultdict[int, int] = defaultdict(int)

    while queue:
        level, node = queue.popleft()
        levels[level] += node.val

        if node.left:
            queue.append((level + 1, node.left))

        if node.right:
            queue.append((level + 1, node.right))

    max_level, _ = max(
        levels.items(), key=lambda x: (x[1], -x[0])
    )  # earliest level preferred

    return max_level


def test():
    root = make([1, 7, 0, 7, -8, None, None])
    assert max_level_sum(root) == 2

    root = make([989, None, 10250, 98693, -89388, None, None, None, -32127])
    assert max_level_sum(root) == 2


test()
