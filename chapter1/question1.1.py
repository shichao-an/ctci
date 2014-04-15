from __future__ import print_function


def is_unique_chars(s):
    """Determine if a string has all unique characters (ASCII)"""
    if len(s) > 256:
        return False
    char_set = [False] * 256
    for c in s:
        if char_set[ord(c)]:
            return False
        char_set[ord(c)] = True
    return True


def _test():
    pass


def _print():
    s1 = 'abcde'
    print(is_unique_chars(s1))
    s2 = 'abcdaf'
    print(is_unique_chars(s2))


if __name__ == '__main__':
    _print()
