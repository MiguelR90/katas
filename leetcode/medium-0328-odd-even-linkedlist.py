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


def append(head: LinkedNode, node: LinkedNode) -> None:
    current: LinkedNode | None = head
    while current.next:
        current = current.next

    current.next = node


def odd_even(head: LinkedNode) -> LinkedNode:
    if not head.next:
        return head

    if not head.next.next:
        return head

    odds: LinkedNode | None = head
    evens: LinkedNode | None = head.next
    current: LinkedNode | None = head.next.next

    # Important to clear the list
    odds.next = None
    evens.next = None

    i: int = 3
    while current:
        next_node = current.next
        current.next = None
        if i % 2 == 0:
            append(evens, current)
        else:
            append(odds, current)

        current = next_node
        i += 1

    current = odds
    while current.next:
        current = current.next

    current.next = evens

    return odds


def to_list(head: LinkedNode) -> list[int]:
    out: list[int] = []
    current = head
    while current:
        out.append(current.val)
        current = current.next

    return out


def test():
    input = [1, 2, 3, 4, 5, 6, 7]
    head = make(input)
    assert to_list(odd_even(head)) == [1, 3, 5, 7, 2, 4, 6]

    input = [1]
    head = make(input)
    assert to_list(odd_even(head)) == [1]

    input = [1, 2]
    head = make(input)
    assert to_list(odd_even(head)) == [1, 2]

    input = [1, 2, 3]
    head = make(input)
    assert to_list(odd_even(head)) == [1, 3, 2]


if __name__ == "__main__":
    test()
