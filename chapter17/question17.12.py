from __future__ import print_function


def get_sum_pairs1(a, s):
    """Return a list of tuples of indices"""
    d = {}
    res = []
    for i, e in enumerate(a):
        if s - e in d:
            res.append((s - e, e))
        else:
            d[e] = True
    return res


def get_sum_pairs2(a, s):
    res = []
    a.sort()
    l = 0
    r = len(a) - 1
    while l < r:
        t = a[l] + a[r]
        if t == s:
            res.append((a[l], a[r]))
            l -= 1
            r -= 1
        elif t < s:
            l += 1
        else:
            r -= 1
    return res


def _test():
    pass


def _print():
    a1 = [2, 4, 3, 5, 8, 1]
    r1 = get_sum_pairs1(a1, 7)
    a2 = [2, 4, 3, 5, 8, 1]
    r2 = get_sum_pairs2(a2, 7)
    print(r1)
    print(r2)


if __name__ == '__main__':
    _test()
    _print()
