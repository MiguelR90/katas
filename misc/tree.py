from __future__ import annotations
from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None


def build_tree(nums: list[int | None]) -> Node:
    if not nums or nums[0] is None:
        raise RuntimeError("Empty list or root node is None")

    root = Node(nums[0])
    queue: deque[Node] = deque([root])
    i = 1

    while queue and i < len(nums):
        current = queue.popleft()

        # Try to attach the left child
        if i < len(nums) and (n := nums[i]) is not None:
            current.left = Node(n)
            queue.append(current.left)
        i += 1

        # Try to attach the right child
        if i < len(nums) and (n := nums[i]) is not None:
            current.right = Node(n)
            queue.append(current.right)
        i += 1

    return root


def print_tree(node: Node | None, level: int = 0, prefix: str = "Root: "):
    if node is not None:
        print_tree(node.right, level + 1, "R--- ")
        print("     " * level + prefix + str(node.value))
        print_tree(node.left, level + 1, "L--- ")


if __name__ == "__main__":
    # tree = build_tree(list(range(25)))
    # print_tree(tree)

    tree = build_tree([0, None, 1, 2, 3, 4])
    print_tree(tree)
