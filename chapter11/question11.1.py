from __future__ import print_function


def merge(a, m, b, n):
    """
    m and n is the number of initialized elements in a and b
    """
    i = m - 1  # Index of the last initialized element of a
    j = n - 1  # Index of the last element of b
    k = m + n - 1  # Index of the last element of the merged array
    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -= 1
        k -= 1
    while j >= 0:
        a[k] = b[j]
        j -= 1
        k -= 1


def _test():
    pass


def _print():
    a = [3, 4, 6, 8, 9]
    m = len(a)
    b = [2, 5, 6, 7, 11, 12]
    n = len(b)
    a += [-1 for i in range(n)]
    merge(a, m, b, n)
    print(a)

if __name__ == '__main__':
    _test()
    _print()
