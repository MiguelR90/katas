import argparse

def mystery(n):
    r = 0
    for i in range(1,n):
        for j in range(i+1,n+1):
            for k in range(1,j+1):
                r += 1
    return r


def myster_formula(n):
    return (4 * n * n * n - 4 * n) / 12.0


def pesky(n):
    r = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            for k in range(j,i+j+1):
                r += 1
    return r


def pesky_formula(n):
    return n * (n + 1) * (2*n + 1) / 6.0 + n * (n + 1) / 2.0


def ex(n):
    r = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            r += 1
    return r


def ex_formula(n):
    return n * (n + 1) / 2.0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int)
    args = parser.parse_args()
    n = args.n
    if n > 1000:
        print('n is too large')
        exit()
    print(mystery(n))
    print(myster_formula(n))
    print(pesky(n))
    print(pesky_formula(n))
    print(ex(n))
    print(ex_formula(n))
