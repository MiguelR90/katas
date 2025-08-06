def greatest_num_candies(candies: list[int], extra_candies: int) -> list[bool]:
    results = [False] * len(candies)
    max_candies = max(candies)
    for i, candy in enumerate(candies):
        if max_candies <= candy + extra_candies:
            results[i] = True

    return results


def test():
    assert greatest_num_candies(candies=[4, 2, 1, 1, 2], extra_candies=1) == [
        True,
        False,
        False,
        False,
        False,
    ]
