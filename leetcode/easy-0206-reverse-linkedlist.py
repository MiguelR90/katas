class LinkedNode:
    def __init__(self, val: int = 0, next=None) -> None:
        self.val: int = val
        self.next: LinkedNode | None = next


def make(values: list[int]) -> LinkedNode:
    head = LinkedNode(values[0], None)

    current = head
    for v in values[1:]:
        current.next = LinkedNode(v, None)
        current = current.next

    return head


def to_list(head: LinkedNode) -> list[int]:
    out: list[int] = []
    current = head
    while current:
        out.append(current.val)
        current = current.next

    return out


def reverse(head: LinkedNode) -> LinkedNode:
    stack: list[LinkedNode] = []

    current: LinkedNode | None = head
    while current:
        stack.append(current)
        current = current.next
        stack[-1].next = None

    rev: LinkedNode = stack.pop()
    last: LinkedNode = rev
    while stack:
        last.next = stack.pop()
        last = last.next

    return rev


def test():
    input = [1, 2, 3, 4, 5, 6, 7]
    head = make(input)
    assert to_list(reverse(head)) == [7, 6, 5, 4, 3, 2, 1]

    input = [1, 2]
    head = make(input)
    assert to_list(reverse(head)) == [2, 1]

    input = [1]
    head = make(input)
    assert to_list(reverse(head)) == [1]


if __name__ == "__main__":
    test()
