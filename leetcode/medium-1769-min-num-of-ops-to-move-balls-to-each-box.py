def move_balls(boxes: str) -> list[int]:
    answer: list[int] = [0] * len(boxes)

    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if i != j and boxes[j] == "1":
                answer[i] = answer[i] + abs(i - j)

    return answer


def test():
    assert move_balls("110") == [1, 1, 3]
    assert move_balls("001011") == [11, 8, 5, 4, 3, 4]


test()
