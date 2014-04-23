from __future__ import print_function


def num_bit_swap(a, b):
    count = 0
    c = a ^ b  # Bits that are different are 1s
    while c != 0:
        count += c & 1  # `count` increments upon a different bit
        c >>= 1  # Right shift `c` by one bit so that LSB can be got
    return count


def num_bit_swap2(a, b):
    count = 0
    c = a ^ b
    while c != 0:
        count += 1
        c &= c - 1  # Clear the rightmost 1 bit
    return count


def _test():
    pass


def _print():
    a = int('1001101', 2)
    b = int('1110110', 2)
    print(num_bit_swap(a, b))
    print(num_bit_swap2(a, b))


if __name__ == '__main__':
    _test()
    _print()
