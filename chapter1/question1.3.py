from __future__ import print_function


def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def is_permutation2(s1, s2):
    """Assume ASCII strings"""
    if len(s1) != len(s2):
        return False
    char_set = [0 for i in range(256)]
    for c in s1:
        char_set[ord(c)] += 1
    for c in s2:
        char_set[ord(c)] -= 1
        if char_set[ord(c)] < 0:
            return False
    return True


def _test():
    pass


def _print():
    s1 = 'abcd'
    s2 = 'cbaa'
    print(is_permutation(s1, s2))
    print(is_permutation2(s1, s2))


if __name__ == '__main__':
    _test()
    _print()
