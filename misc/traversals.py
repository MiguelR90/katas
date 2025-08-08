from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(
        self, val: int, left: TreeNode | None = None, right: TreeNode | None = None
    ):
        self.val: int = val
        self.left: TreeNode | None = left
        self.right: TreeNode | None = right


def dfs_inorder(root: TreeNode | None) -> list[int]:
    results: list[int] = []

    def dfs(node: TreeNode | None):
        if node is None:
            return

        dfs(node.left)
        results.append(node.val)
        dfs(node.right)

    dfs(root)
    return results


def dfs_preorder(root: TreeNode | None) -> list[int]:
    results: list[int] = []

    def dfs(node: TreeNode | None):
        if node is None:
            return

        results.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return results


def dfs_postorder(root: TreeNode | None) -> list[int]:
    results: list[int] = []

    def dfs(node: TreeNode | None):
        if node is None:
            return

        dfs(node.left)
        dfs(node.right)
        results.append(node.val)

    dfs(root)
    return results


def bfs_level_order(root: TreeNode | None) -> list[int]:
    if root is None:
        return []

    queue: deque[TreeNode] = deque([root])

    results: list[int] = []
    while queue:
        node = queue.popleft()
        results.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return results


def test_traversals():
    root = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6))
    )

    assert dfs_inorder(root) == [4, 2, 5, 1, 3, 6]
    assert dfs_inorder(TreeNode(1)) == [1]
    assert dfs_inorder(None) == []

    assert dfs_preorder(root) == [1, 2, 4, 5, 3, 6]
    assert dfs_preorder(TreeNode(1)) == [1]
    assert dfs_preorder(None) == []

    assert dfs_postorder(root) == [4, 5, 2, 6, 3, 1]
    assert dfs_postorder(TreeNode(1)) == [1]
    assert dfs_postorder(None) == []

    assert bfs_level_order(root) == [1, 2, 3, 4, 5, 6]
    assert bfs_level_order(TreeNode(1)) == [1]
    assert bfs_level_order(None) == []
