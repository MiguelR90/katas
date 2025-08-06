def reverse_words(s: str) -> str:
    words = s.split(" ")
    return " ".join(w for w in reversed(words) if w)


def test():
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words(" hello world ") == "world hello"
    assert reverse_words("a good  example") == "example good a"
