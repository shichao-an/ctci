from __future__ import print_function


def count_compression(s):
    """Assume len(s) > 0"""
    last = s[0]
    n = len(s)
    size = 0
    count = 1
    for i in range(1, n):
        if s[i] == last:
            count += 1
        else:
            size += 1 + len(str(count))
            last = s[i]
            count = 1
    size += 1 + len(str(count))
    return size


def compress_string(s):
    """
    Use a temporary list to hold compressed characters
    """
    if not s:
        return s
    n = len(s)
    size = count_compression(s)
    if size >= n:
        return s

    t = [None for i in range(size)]
    last = s[0]
    count = 1
    index = 0
    for i in range(1, n):
        if s[i] == last:
            count += 1
        else:
            t[index] = last
            index += 1
            cs = str(count)
            for c in cs:
                t[index] = c
                index += 1
            last = s[i]
            count = 1

    # Process the last ones
    t[index] = last
    index += 1
    cs = str(count)
    for c in cs:
        t[index] = c
        index += 1
    return ''.join(t)


def _test():
    pass


def _print():
    s = 'aabcccccaaa'
    print(compress_string(s))


if __name__ == '__main__':
    _test()
    _print()
