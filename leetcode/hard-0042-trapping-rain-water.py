from collections import deque
from itertools import chain


def rain_orig(heights: list[int]) -> int:
    stack: deque[int] = deque()
    total: int = 0

    print("----")
    for h in chain(heights, [0]):
        if (
            stack
            and h < stack[-1]
            and (
                min(stack) < stack[0] < max(stack)
                or min(stack) < stack[-1] < max(stack)
            )
        ):
            H = min(stack[0], stack[-1])
            while len(stack) > 1:
                total += max(H - stack.popleft(), 0)

            stack.append(h)

        elif not stack and h == 0:
            continue
        else:
            stack.append(h)

        print(f"{h=} {stack=} {total=}")

    return total


def rain(heights: list[int]) -> int:
    stack = []
    total = 0

    for i, h in enumerate(heights):
        # While the stack is not empty and current height is greater than top of stack
        while stack and h > heights[stack[-1]]:
            bottom = stack.pop()

            if not stack:
                break  # No left wall to trap water

            left = stack[-1]
            width = i - left - 1
            bounded_height = min(heights[left], h) - heights[bottom]
            total += width * bounded_height

        stack.append(i)

    return total


def test():
    assert rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert rain([4, 2, 0, 3, 2, 5]) == 9
