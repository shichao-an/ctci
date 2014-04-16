from __future__ import print_function


def replace_spaces(s, n):
    s = list(s)
    nl = 0  # New length of the string
    sp = 0  # Count of spaces
    for c in s[:n]:
        if c == ' ':
            sp += 1
    nl = n + sp * 2
    for i in range(n - 1, -1, -1):
        c = s[i]
        if c == ' ':
            s[nl - 1] = '0'
            s[nl - 2] = '2'
            s[nl - 3] = '%'
            nl -= 3
        else:
            s[nl - 1] = c
            nl -= 1
    return ''.join(s)


def _test():
    pass


def _print():
    s = 'hello world, this is fun!'
    n = len(s)
    es = ' ' * 8
    s += es
    print(replace_spaces(s, n))


if __name__ == '__main__':
    _test()
    _print()
