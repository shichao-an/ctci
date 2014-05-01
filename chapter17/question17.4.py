from __future__ import print_function
import sys


def get_int_bits():
    """
    Get number of bits to store an int on the Python implementation of the
    current machine
    """
    if sys.maxsize >> 62 == 0:
        return 32
    else:
        return 64


def get_sign(n):
    """Postive int will have a sign 1 and negative 0"""
    bits = get_int_bits()
    return ((n >> bits) & 1) ^ 1


def get_max1(a, b):
    k = get_sign(a - b)
    q = k ^ 1
    return k * a + b * q


def get_max2(a, b):
    """It seems Python int does not overflow..."""
    sa = get_sign(a)
    sb = get_sign(b)
    sc = get_sign(a - b)
    # If a and b have different signs, ka will be 1, kc will be 0,
    # and thus k = sign(a)
    ka = sa ^ sb
    # If a and b have the same sign, kc will be 1, ka will be 0,
    # and thus k = sign(a - b)
    kc = ka ^ 1

    k = ka * sa + kc * sc
    q = k ^ 1
    return a * k + b * q


def _test():
    pass


def _print():
    print(get_int_bits())
    print(get_sign(127))
    print(get_sign(-9))
    print(get_max1(9, 8))
    print(get_max1(-7, -3))


if __name__ == '__main__':
    _test()
    _print()
