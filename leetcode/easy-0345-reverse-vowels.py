import itertools


VOWELS: set[str] = set(itertools.chain("aeiou", "aeiou".upper()))


def reverse_vowels(s: str) -> str:
    s_list: list[str] = list(s)

    letters: list[str] = []
    idx: list[int] = []
    for i, letter in enumerate(s_list):
        if letter in VOWELS:
            idx.append(i)
            letters.append(letter)

    for i, letter in zip(reversed(idx), letters):
        s_list[i] = letter

    return "".join(s_list)


def test():
    assert reverse_vowels("IceCreAm") == "AceCreIm"
    assert reverse_vowels("leetcode") == "leotcede"
