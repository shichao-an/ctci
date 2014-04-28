from __future__ import print_function


def make_change(n, changes):
    """
    `changes` is a list of integers
    """
    if not changes:
        return 0
    elif n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return (make_change(n - changes[-1], changes)
                + make_change(n, changes[:-1]))


def make_change2_aux(n, changes, m, t):
    """Top-Down DP"""
    if m < 0:
        return 0
    elif n < 0:
        return 0
    elif n == 0:
        return 1
    elif t[n][m] != 0:
        return t[n][m]
    else:
        t[n][m] = (make_change2_aux(n - changes[m], changes, m, t)
                   + make_change2_aux(n, changes, m - 1, t))
        return t[n][m]


def make_change2(n, changes):
    t = [[0 for i in changes] for i in range(n + 1)]
    return make_change2_aux(n, changes, len(changes) - 1, t)


def make_change3_aux(n, changes, m):
    """Bottom-Up DP"""
    t = [[0 for i in changes] for i in range(n + 1)]
    for i in range(0, n + 1):
        for j in range(m + 1):
            if i == 0:
                t[i][j] = 1
            else:
                x = y = 0
                if i - changes[j] >= 0:
                    x = t[i - changes[j]][j]
                if j - 1 >= 0:
                    y = t[i][j - 1]
                t[i][j] = x + y
    return t[n][m]


def make_change3(n, changes):
    return make_change3_aux(n, changes, len(changes) - 1)


def _test():
    pass


def _print():
    c1 = [1, 5, 10, 25]
    n1 = 500
    r1 = make_change(n1, c1)
    print(r1)
    r2 = make_change2(n1, c1)
    print(r2)
    r3 = make_change3(n1, c1)
    print(r3)


if __name__ == '__main__':
    _test()
    _print()
