close2open = {")": "(", "}": "{", "]": "["}
opens = set(close2open.values())


def valid(s: str) -> bool:
    stack: list[str] = []

    for char in s:
        if char in opens:
            stack.append(char)
        elif stack and stack[-1] == close2open[char]:
            _ = stack.pop()
        else:
            return False

    return len(stack) == 0


def test():
    assert valid("()") is True
    assert valid("()[]{}") is True
    assert valid("(]") is False
    assert valid("([])") is True
