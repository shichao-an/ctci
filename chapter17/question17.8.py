from __future__ import print_function


def get_max_sum1(a):
    """Zero-length sequence allowed"""
    s = 0  # Current sum
    ms = 0  # Maximum sum
    for e in a:
        s = max(0, s + e)
        ms = max(s, ms)
    return ms


def get_max_sum2(a):
    """Zero-length sequence not allowed"""
    s = ms = a[0]
    n = len(a)
    for i in range(1, n):
        s = max(a[i], s + a[i])
        ms = max(s, ms)
    return ms


def get_max_sum3(a):
    """
    `get_max_sum2` variant that returns start and end of
    the target sequence
    """
    s = ms = a[0]
    n = len(a)
    mstart = 0
    mend = 0
    start = 0
    end = 0
    for i in range(1, n):
        if s + a[i] < a[i]:
            s = a[i]
            start = i
            end = i
        else:
            s = s + a[i]
            end = i
        if ms < s:
            ms = s
            mstart = start
            mend = end
    return mstart, mend


def get_max_sum4(a):
    """Zero-length sequence allowed; `get_max_sum2` variant"""
    return max(get_max_sum2(a), 0)


def _test():
    pass


def _print():
    a1 = [5, -9, 6, -2, 3]
    print(get_max_sum1(a1))
    print(get_max_sum2(a1))
    print(get_max_sum3(a1))
    a2 = [-7, -2, -4, -5]
    print(get_max_sum1(a2))
    print(get_max_sum2(a2))
    print(get_max_sum3(a2))
    a3 = [1, 2, -3, 2, 2, -1]
    print(get_max_sum1(a3))
    print(get_max_sum2(a3))
    print(get_max_sum3(a3))


if __name__ == '__main__':
    _test()
    _print()
