def product_except_self(nums: list[int]) -> list[int]:
    answer: list[int] = [1] * len(nums)

    # this is o(n^2) - which can be done with o(n)
    for i in range(len(nums)):
        for j, n in enumerate(nums):
            if i != j:
                answer[i] *= n

    return answer


def product_except_self2(nums: list[int]) -> list[int]:
    # cummulative products forwards and backwards
    forwards: list[int] = [-1] * len(nums)
    tmp = 1
    for i, v in enumerate(nums):
        tmp *= v
        forwards[i] = tmp

    backwards: list[int] = [-1] * len(nums)
    tmp = 1
    for i, v in reversed(list(enumerate(nums))):  # this allocates extra memeory
        tmp *= v
        backwards[i] = tmp

    # alternative implementation using itertools.accumulate
    # from itertools import accumulate
    # import operator
    # forwards = list(accumulate(nums, func=operator.mul))
    # backwards = list(reversed(list(accumulate(reversed(nums), func=operator.mul))))

    answer: list[int] = [-1] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            answer[i] = backwards[1]
        elif i == len(nums) - 1:
            answer[i] = forwards[i - 1]
        else:
            answer[i] = forwards[i - 1] * backwards[i + 1]

    return answer


def test():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self2([1, 2, 3, 4]) == [24, 12, 8, 6]

    test = list(range(100))
    assert product_except_self2(test) == product_except_self(test)

    test = list(range(100))
    assert product_except_self2(test) == product_except_self(test)
