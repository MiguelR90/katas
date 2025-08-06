def longest_common_prefix(strs: list[str]) -> str:
    i: int = 0
    while all(s[: i + 1] == strs[0][: i + 1] for s in strs[1:]):
        i += 1

    return strs[0][:i]


def test():
    assert longest_common_prefix(["flowers", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "rececar", "car"]) == ""
    assert longest_common_prefix(["flow", "flows", "flower"]) == "flow"
    assert longest_common_prefix(["abc", "abc", "ab"]) == "ab"
    assert longest_common_prefix(["", "a"]) == ""
