from itertools import combinations


def max_subsequence(nums1: list[int], nums2: list[int], k: int) -> int:
    n: int = len(nums1)
    best: int = 0

    for seq in combinations(range(n), k):
        score: int = sum(nums1[s] for s in seq) * min(nums2[s] for s in seq)
        best = max(best, score)

    return best


def test():
    assert max_subsequence([1, 3, 3, 2], [2, 1, 3, 4], 3) == 12


test()
