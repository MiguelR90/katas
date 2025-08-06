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


def search(head: LinkedNode, index: int) -> LinkedNode:
    i: int = 0
    current: LinkedNode | None = head
    while current:
        if i == index:
            return current

        i += 1
        current = current.next

    raise IndexError(f"No node at {index=}")


def size(head: LinkedNode) -> int:
    n: int = 0
    current: LinkedNode | None = head
    while current:
        n += 1
        current = current.next

    return n


def to_list(head: LinkedNode) -> list[int]:
    out: list[int] = []
    current = head
    while current:
        out.append(current.val)
        current = current.next

    return out


def max_twin_sum(head: LinkedNode) -> int:
    i: int = 0
    n: int = size(head)
    sums: list[int] = []
    while i < (n - 1 - i):
        a = search(head, i)
        b = search(head, n - 1 - i)
        sums.append(a.val + b.val)
        i += 1

    return max(sums)


def test():
    input = [5, 4, 2, 1]
    head = make(input)
    assert max_twin_sum(head) == 6

    input = [4, 2, 2, 3]
    head = make(input)
    assert max_twin_sum(head) == 7


if __name__ == "__main__":
    test()
