def fib(n: int) -> int:
    if n < 2:
        return n

    prev, current = 0, 1
    for i in range(2, n + 1):
        prev, current = current, prev + current

    return current


def test():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(10) == 55
    assert fib(15) == 610
    assert fib(20) == 6765


if __name__ == "__main__":
    test()
    print("All tests passed!")
