from __future__ import print_function


def swap1(a, b):
    a = a - b
    b = b + a
    a = b - a
    return a, b


def swap2(a, b):
    """Bit manipulation: integers only"""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def _test():
    pass


def _print():
    a1, b1 = 2.3, 4.9
    print(swap1(a1, b1))
    a2, b2 = 2, 4
    print(swap2(a2, b2))


if __name__ == '__main__':
    _test()
    _print()
