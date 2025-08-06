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


def delete(root: TreeNode | None, key: int) -> TreeNode | None:
    match root:
        case None:
            return None
        case TreeNode(val=val) if key < val:
            root.left = delete(root.left, key)
            return root
        case TreeNode(val=val) if val < key:
            root.right = delete(root.right, key)
            return root
        case TreeNode(left=None):
            return root.right
        case TreeNode(right=None):
            return root.left
        case TreeNode(left=TreeNode(), right=TreeNode()):
            successor: TreeNode = root.right
            while successor.left:
                successor = successor.left

            successor.right = delete(root.right, successor.val)
            successor.left = root.left
            return successor
        case _:
            raise RuntimeError


def print_tree(node: TreeNode | None, prefix: str = "", is_left: bool = True) -> None:
    if not node:
        return

    if node.right:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(node.val))

    if node.left:
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


def test():
    root = make([5, 3, 6, 2, 4, None, 7])
    # print_tree(root)
    root = delete(root, 3)
    # print_tree(root)

    assert root.val == 5
    assert root.left.val == 4
    assert root.right.val == 6

    # print("-----")
    root = make([3, 1, 5, 0, 2, 4, 6, -1, None, None, None, None, None, None, 7])
    # print_tree(root)
    for i in [6, 2, 3, 0, -1, 4]:
        root = delete(root, i)
        # print(f"delete {i=}")
        # print_tree(root)

    assert root.val == 5
    assert root.left.val == 1
    assert root.right.val == 7


test()
