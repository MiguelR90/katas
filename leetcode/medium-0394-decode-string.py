import re


pattern = r"(\d+)\[(\w+)\]"


def decode_string(s: str) -> str:
    while match := re.search(pattern, s):
        decode: str = match.group(2) * int(match.group(1))
        i, j = match.span()
        s = f"{s[:i]}{decode}{s[j:]}"

    return s


def test():
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]2[cd]ef") == "abcabccdcdef"
