from __future__ import print_function


def print_binary(num):
    if num >= 1 or num <= 0:
        return 'ERROR'
    b = []
    b.append('0')
    b.append('.')
    while num > 0:
        if len(b) >= 32:
            return 'ERROR'
        r = num * 2
        if r >= 1:
            b.append('1')
            num = r - 1
        else:
            b.append('0')
            num = r
    return ''.join(b)


def _test():
    pass


def _print():
    print(print_binary(0.625))


if __name__ == '__main__':
    _test()
    _print()
