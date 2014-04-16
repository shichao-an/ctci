from __future__ import print_function


def is_substring(s, ss):
    """Determine whether `ss` is a substring of s"""
    return ss in s


def is_rotation(s1, s2):
    """
    Determine whether s2 is a rotation of s1
    s1 = xy
    s2 = yx
    s1s1 = xyxy
    """
    if len(s1) != len(s2):
        return False
    return is_substring(s1 + s1, s2)


def _test():
    pass


def _print():
    s1 = 'waterbottle'
    s2 = 'erbottlewat'
    s3 = 'waterbttleo'
    print(is_rotation(s1, s2))
    print(is_rotation(s1, s3))


if __name__ == '__main__':
    _test()
    _print()
