from __future__ import print_function


def find_unsorted_sequence(a):
    m = 0  # Start of sequence
    n = len(a) - 1  # End of sequence

    # Find the temporary start
    while m < n:
        if a[m] <= a[m + 1]:
            m += 1
        else:
            break
    while n > m:
        if a[n] >= a[n - 1]:
            n -= 1
        else:
            break
    if m == n:
        return -1, -1  # Already sorted
    min_value = a[m + 1]
    max_value = a[n - 1]
    for i in range(m + 1, n):
        min_value = min(min_value, a[i])
        max_value = max(max_value, a[i])
    while m >= 0 and a[m] > min_value:
        m -= 1
    while n < len(a) and a[n] < max_value:
        n += 1
    return m + 1, n - 1


def _test():
    pass


def _print():
    a1 = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    r1 = find_unsorted_sequence(a1)
    a2 = [1, 2, 3, 4]
    r2 = find_unsorted_sequence(a2)
    a3 = [1]
    r3 = find_unsorted_sequence(a3)
    a4 = [4, 3, 1, 2]
    r4 = find_unsorted_sequence(a4)
    a5 = [2, 4, 5, 3, 8, 9]
    r5 = find_unsorted_sequence(a5)
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)


if __name__ == '__main__':
    _test()
    _print()
