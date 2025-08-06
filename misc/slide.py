from collections.abc import Iterable


def generate_ranges(stream: list[tuple[int, str]]) -> Iterable[tuple[int, int, int]]:
    for i, (start, _) in enumerate(stream):
        yield i, start, start + 10


def sliding_window(stream: list[tuple[int, str]]) -> list[tuple[int, int, bool]]:
    out: list[tuple[int, int, bool]] = []

    for i, start, end in generate_ranges(stream):
        valid: bool = True
        stack: list[str] = []
        for t, char in stream[i:]:
            if start <= t and t <= end and char == "(":
                stack.append(char)
            elif start <= t and t <= end and char == ")":
                if len(stack) == 0 or stack.pop() != "(":
                    valid = False
            else:
                break
        if len(stack) > 0:
            valid = False
        out.append((start, end, valid))

    return out


out = sliding_window([(1, "("), (5, ")"), (12, "("), (15, ")")])
print(out)
