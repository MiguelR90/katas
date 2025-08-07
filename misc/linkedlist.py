from __future__ import annotations
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar("T")


@dataclass
class LinkedListNode(Generic[T]):
    val: T
    next: LinkedListNode[T] | None = None


def test_linked_list():
    root = LinkedListNode(1)
    root.next = LinkedListNode(2)
    root.next.next = LinkedListNode(3)

    current = root
    values = []
    while current:
        values.append(current.val)
        current = current.next

    assert values == [1, 2, 3], f"Expected [1, 2, 3], got {values}"


if __name__ == "__main__":
    test_linked_list()
