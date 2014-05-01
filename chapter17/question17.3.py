from __future__ import print_function
import math


def count_fact_zeros(n):
    count = 0
    i = 5
    while n / i > 0:
        count += n / i
        i *= 5
    return count


def _test():
    pass


def _print():
    print(count_fact_zeros(15))
    print(math.factorial(15))
    print(count_fact_zeros(27))
    print(math.factorial(27))
    print(count_fact_zeros(126))


if __name__ == '__main__':
    _test()
    _print()
