from __future__ import print_function


def is_pow2(n):
    return n & (n - 1) == 0


def _test():
    assert not is_pow2(3)
    assert is_pow2(4)
    assert is_pow2(8)


def _print():
    pass


if __name__ == '__main__':
    _test()
    _print()
