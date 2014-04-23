from __future__ import print_function


def negate(a):
    """Negate an integer using add operator"""
    res = 0
    d = 1 if a < 0 else -1
    while a != 0:
        res += d
        a += d
    return res


def absolute(a):
    if a < 0:
        return negate(a)
    return a


def minus(a, b):
    return a + negate(b)


def multiply(a, b):
    _a = absolute(a)
    _b = absolute(b)
    if _a < _b:
        return multiply(b, a)
    res = 0
    for i in range(_b):
        res += a
    if b < 0:
        res = negate(res)
    return res


def divide(a, b):
    if b == 0:
        return 'ERROR'
    _a = absolute(a)
    _b = absolute(b)
    res = 0
    t = 0
    while t + _b <= _a:
        t += _b
        res += 1
    if a < 0 and b > 0 or a > 0 and b < 0:
        res = negate(res)
    return res


def _test():
    pass


def _print():
    print(multiply(4, 2))
    print(multiply(-2, -4))
    print(multiply(2, -4))
    print(divide(5, 2))
    print(divide(-6, 2))
    print(divide(7, -6))
    print(divide(7, 7))
    print(divide(0, 2))


if __name__ == '__main__':
    _test()
    _print()
