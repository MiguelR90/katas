def str_matching(words: list[str]) -> list[str]:
    out: list[str] = []
    for i, subs in enumerate(words):
        for j, word in enumerate(words):
            if i != j and subs in word:
                out.append(subs)
    return out


def test():
    assert str_matching(["mass", "as", "hero", "superhero"]) == ["as", "hero"]
    assert str_matching(["leetcode", "et", "code"]) == ["et", "code"]
    assert str_matching(["blue", "green", "bu"]) == []


test()
