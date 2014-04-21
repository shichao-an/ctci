from __future__ import print_function


def update_bits(n, m, i, j):
    bit_num = j - i + 1  # Number of bits to clear
    mask = (2 << bit_num - 1) << i
    mask = ~mask
    n &= mask  # Clear bits for m
    m <<= i
    return m | n


def _test():
    pass


def _print():
    n = int('10000000000', 2)
    m = int('10011', 2)
    i = 2
    j = 6
    res = update_bits(n, m, i, j)
    print(bin(res))


if __name__ == '__main__':
    _test()
    _print()
