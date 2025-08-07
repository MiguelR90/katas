operators: set[str] = {"*", "+", "-", "/"}


def polish_eval(tokens: list[str]) -> float:
    stack: list[str] = []

    for t in tokens:
        if t not in operators:
            stack.append(t)
        else:
            b = stack.pop()
            a = stack.pop()
            result = str(int(float(eval(f"{a} {t} {b}"))))
            stack.append(result)

    return int(stack.pop())


def test():
    assert polish_eval(["2", "1", "+", "3", "*"]) == 9
    assert polish_eval(["4", "13", "5", "/", "+"]) == 6
    assert (
        polish_eval(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
        == 22
    )
