from heapq import heapify, heappop


# def universals(words1: list[str], words2: list[str]) -> list[str]:
#     uni: list[str] = []
#
#     for a in words1:
#         for b in words2:
#             bb: str = "".join(sorted(b))
#             aa: str = "".join(c for c in sorted(a) if c in bb)
#
#             if bb not in aa:
#                 break
#
#         else:
#             uni.append(a)
#
#     return uni


def universals(words1: list[str], words2: list[str]) -> list[str]:
    uni: list[str] = []

    for a in words1:
        for b in words2:
            aa, bb = list(a), list(b)
            _, _ = heapify(aa), heapify(bb)
            while aa and bb:
                if aa[0] == bb[0]:
                    _, _ = heappop(aa), heappop(bb)
                else:
                    _ = heappop(aa)

            if bb:
                break

        else:
            uni.append(a)

    return uni


def test():
    assert universals(
        ["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]
    ) == ["facebook", "google", "leetcode"]
    assert universals(
        ["amazon", "apple", "facebook", "google", "leetcode"], ["lc", "eo"]
    ) == ["leetcode"]
    assert universals(
        ["acaac", "cccbb", "aacbb", "caacc", "bcbbb"], ["c", "cc", "b"]
    ) == ["cccbb"]


test()
