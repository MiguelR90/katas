def max_score(s: str) -> int:
    score: int = -1
    for i in range(1, len(s)):
        a = sum(c == "0" for c in s[:i])
        b = sum(c == "1" for c in s[i:])
        score = max(a + b, score)

    return score


def test():
    assert max_score("011101") == 5
    assert max_score("00111") == 5
    assert max_score("1111") == 3


test()
