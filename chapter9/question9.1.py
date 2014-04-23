from __future__ import print_function


def count_ways(n):
    """DP, Iterative"""
    if n < 0:
        return 0
    t = [0 for i in range(n + 1)]
    t[0] = 1
    t[1] = 1
    t[2] = 2
    if n < 3:
        return t[n]
    for i in range(3, n + 1):
        t[i] = t[i - 3] + t[i - 2] + t[i - 1]
    return t[n]


def count_ways2(n):
    """Recursive, O(3^n) time"""
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_ways2(n - 3) + count_ways2(n - 2) + count_ways2(n - 1)


def count_ways3_aux(n, t):
    """DP, Recursive"""
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif t[n] != -1:
        return t[n]
    else:
        t[n] = (count_ways3_aux(n - 3, t)
                + count_ways3_aux(n - 2, t)
                + count_ways3_aux(n - 1, t))
        return t[n]


def count_ways3(n):
    if n < 0:
        return 0
    t = [-1 for i in range(n + 1)]
    return count_ways3_aux(n, t)


def _test():
    pass


def _print():
    print(count_ways(2))
    print(count_ways(3))
    print(count_ways(4))
    print(count_ways(5))
    print(count_ways2(2))
    print(count_ways2(3))
    print(count_ways2(4))
    print(count_ways2(5))
    print(count_ways3(2))
    print(count_ways3(3))
    print(count_ways3(4))
    print(count_ways3(5))


if __name__ == '__main__':
    _test()
    _print()
