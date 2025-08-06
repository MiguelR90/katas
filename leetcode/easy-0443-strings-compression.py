def compress(chars: list[str]) -> list[str | int]:
    out: list[str | int] = []

    count = 1
    previous = ""
    for i, current in enumerate(chars):
        if current != previous and count == 1:
            out.append(current)
            count = 1
        elif current != previous and count > 1:
            out.append(current)
            out.append(count)
            count = 1
        elif count == 9:
            out.append(count)
            count = 1
        elif i == len(chars) - 1 and count > 1:
            out.append(count)
            count += 1
        else:
            count += 1

        previous = current

    return out


def test():
    assert len(compress(["a", "a", "b", "b", "c", "c", "c"])) == 6
    assert len(compress(["a"])) == 1
    assert (
        len(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
        == 4
    )
