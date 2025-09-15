"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

"""


def repeated(s: str) -> list[str]:
    out: set[str] = set()
    seen: set[str] = set()

    for i in range(len(s) - 10 + 1):
        if (seq := s[i : i + 10]) in seen:
            out.add(seq)
        else:
            seen.add(seq)

    return list(out)


def test():
    assert set(repeated("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) == set(
        ["AAAAACCCCC", "CCCCCAAAAA"]
    )
