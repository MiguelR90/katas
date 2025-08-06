from copy import copy


def divides(s: str, t: str) -> bool:
    # t divides s if s = t + t + ...
    # consider copying t? since we're mutating it
    k = copy(t)
    while len(k) <= len(s):
        if k == s:
            return True
        k += t
    return False


# the greatest common divisor needs to be a prefix of each strings so try all prefixes
def gcd(str1: str, str2: str) -> str:
    # ensure that str1 is always the longest strings
    if len(str1) < len(str2):
        str1, str2 = str2, str1

    for i in range(len(str2)):
        prefix: str = str2[: len(str2) - i]
        if divides(str1, prefix) and divides(str2, prefix):
            return prefix

    return ""


def test():
    assert gcd("abcabc", "abc") == "abc"
    assert gcd("ababab", "abab") == "ab"
    assert gcd("leet", "code") == ""
