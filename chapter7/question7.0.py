from __future__ import print_function


def cross_off(flags, prime):
    """
    Cross of (set to False) those indexes that
    are divisible by `prime`
    """
    i = prime * prime
    while i < len(flags):
        flags[i] = False
        i += prime


def get_next_prime(flags, prime):
    """Find the index of the first True in flags after `prime`"""
    np = prime + 1
    while np < len(flags) and flags[np] is False:
        np += 1
    return np


def generate_primes(n):
    """Generate a list of primes between 1 and n"""
    flags = [True for i in range(n)]
    flags[0] = False
    flags[1] = False
    prime = 2
    while prime < n:
        cross_off(flags, prime)
        prime = get_next_prime(flags, prime)
    for i, e in enumerate(flags):
        if e is True:
            yield i


def _test():
    pass


def _print():
    primes = list(generate_primes(20))
    print(primes)


if __name__ == '__main__':
    _test()
    _print()
