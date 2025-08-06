def repeated_dna(s: str) -> list[str]:
    seqs: dict[str, int] = {}

    for i in range(len(s) - 10):
        seq = s[i : i + 10]
        seqs[seq] = seqs.get(seq, 0) + 1

    return list(k for k, v in seqs.items() if v > 1)


def test():
    assert repeated_dna("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == [
        "AAAAACCCCC",
        "CCCCCAAAAA",
    ]
    assert repeated_dna("AAAAAAAAAAAAA") == ["AAAAAAAAAA"]
