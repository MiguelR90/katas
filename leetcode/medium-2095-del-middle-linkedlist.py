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


def size(head: LinkedNode) -> int:
    n: int = 0
    current: LinkedNode | None = head
    while current:
        n += 1
        current = current.next

    return n


def delete_middle(head: LinkedNode) -> LinkedNode:
    middle: int = size(head) // 2

    # handle the case when size(head) == 1

    previous: LinkedNode | None = head
    current: LinkedNode | None = head.next
    i: int = 1
    while current:
        if i == middle:
            previous.next = current.next
            break

        previous = current
        current = current.next
        i += 1

    return head


def to_list(head: LinkedNode) -> list[int]:
    out: list[int] = []
    current = head
    while current:
        out.append(current.val)
        current = current.next

    return out


def test():
    input = [1, 3, 4, 7, 1, 2, 6]
    head = make(input)
    assert size(head) == len(input)

    head = delete_middle(head)
    assert size(head) == len(input) - 1

    assert to_list(head) == [1, 3, 4, 1, 2, 6]

    input = [1, 3]
    head = make(input)
    assert size(head) == len(input)

    head = delete_middle(head)
    assert size(head) == len(input) - 1

    assert to_list(head) == [1]
