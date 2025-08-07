from collections.abc import Iterable


def valid(s: str) -> bool:
    stack: list[str] = []

    for chr in s:
        if chr in {"(", "[", "{"}:
            stack.append(chr)
            continue
        elif stack:
            oopen: str = stack.pop()
        else:
            # stack is empty => nothing to match against
            return False

        if chr == ")" and oopen != "(":
            return False
        elif chr == "]" and oopen != "[":
            return False
        elif chr == "}" and oopen != "{":
            return False

    return len(stack) == 0


def generate_subs(s: str, k: int) -> Iterable[str]:
    for i in range(len(s) - k + 1):
        yield s[i : i + k]


def longest(s: str) -> int:
    maxlen: int = 0

    for k in range(1, len(s) + 1):
        for subs in generate_subs(s, k):
            if valid(subs):
                maxlen = len(subs)
                break

    return maxlen


def test():
    assert longest("(()") == 2
    assert longest(")()())") == 4
    assert longest("") == 0
