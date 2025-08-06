def max_k_sums(nums: list[int], k: int) -> int:
    operations: int = 0
    tumbstones: set[int] = set()

    for i, x in enumerate(nums[:-1]):
        if i in tumbstones:
            continue

        for j, y in enumerate(nums[i + 1 :], i + 1):
            if j in tumbstones:
                continue

            if x + y == k:
                operations += 1
                tumbstones.add(i)
                tumbstones.add(j)
                break  # once you find it you need to break

    return operations


def test():
    assert max_k_sums([1, 2, 3, 4], 5) == 2
    assert max_k_sums([3, 1, 3, 4, 3], 6) == 1
    assert max_k_sums([1, 1, 1, 1, 1], 2) == 2
