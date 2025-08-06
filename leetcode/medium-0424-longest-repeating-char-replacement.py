from collections import Counter
from collections.abc import Iterable


def generate_subs(s: str, k: int) -> Iterable[str]:
    for i in range(len(s) - k + 1):
        yield s[i : i + k]


def is_valid(subs: str, k: int) -> bool:
    return len(subs) <= max(Counter(subs).values()) + k


def replace(s: str, k: int) -> int:
    # you can always replace k chars
    longest: int = k

    for kk in range(k + 1, len(s) + 1):
        for subs in generate_subs(s, kk):
            if is_valid(subs, k):
                longest = kk

                # Opt: stop checking kk-subs
                break

    return longest


def test():
    assert replace("ABAB", 2) == 4
    assert replace("AABABBA", 1) == 4
