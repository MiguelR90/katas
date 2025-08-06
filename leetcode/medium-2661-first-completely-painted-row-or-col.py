def update(mat: list[list[int]], value: int) -> list[list[int]]:
    m: int = len(mat)
    n: int = len(mat[0])

    for i, j in ((i, j) for i in range(m) for j in range(n)):
        if mat[i][j] == value:
            mat[i][j] = -1
            break

    return mat


def check(mat: list[list[int]]) -> bool:
    m: int = len(mat)
    n: int = len(mat[0])

    # row-wise
    for i in range(m):
        if all(mat[i][j] == -1 for j in range(n)):
            return True

    # col-wise
    for j in range(n):
        if all(mat[i][j] == -1 for i in range(m)):
            return True

    return False


def paint(arr: list[int], mat: list[list[int]]) -> int:
    for i, value in enumerate(arr):
        if (mat := update(mat, value)) and check(mat):
            return i

    return -1


def test():
    assert paint([1, 3, 4, 3], [[1, 4], [2, 3]]) == 2
    assert paint([2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]]) == 3


test()
