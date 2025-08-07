def valid(s: str) -> bool:
    stack: list[str] = []

    for chr in s:
        if chr in {"(", "[", "{"}:
            stack.append(chr)
        elif chr == ")":
            if stack.pop() != "(":
                return False
        elif chr == "]":
            if stack.pop() != "[":
                return False
        elif chr == "}":
            if stack.pop() != "{":
                return False

    return len(stack) == 0


def test():
    assert valid("()") is True
    assert valid("()[]{}") is True
    assert valid("(]") is False
    assert valid("([])") is True
    assert valid("([)]") is False
