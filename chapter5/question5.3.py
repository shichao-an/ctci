from __future__ import print_function


def get_next(n):
    c = n
    c0 = 0  # Number of rightmost consecutive zeros (may be 0) if
            # the least significant bit is 1
    c1 = 0  # Number of rightmost consecutive ones

    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1
    while c & 1 == 1:
        c1 += 1
        c >>= 1

    # If n is any of the following:
    # 1. All zeroes
    # 2. All ones
    # 3. Consecutive ones followed by consecutive zeroes,
    #    e.g. 11..1100..00 (filled 31 up to 31 bits of
    #    an 32-bit signed integer)
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1  # ERROR
    p = c0 + c1
    # Flip `p`, which is the rightmost non-trailing zero bit
    n |= 1 << p
    n &= ~((1 << p) - 1)
    n |= (1 << (c1 - 1)) - 1
    return n


def _test():
    pass


def _print():
    n1 = 13948
    print(bin(n1))
    r1 = get_next(n1)
    print(bin(r1))


if __name__ == '__main__':
    _test()
    _print()
