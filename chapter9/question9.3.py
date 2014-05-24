from __future__ import print_function

"""
A magic index in an array A[1...n - 1] is defined to be an index such that
A[i] = i. Give a sorted array of distinct integers, write a method to find a
magic index, if one exists, in array A.

FOLLOW UP

What if the values are not distinct?
"""


def find_magic1(a):
    """Distinct values"""
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) / 2
        if a[mid] == mid:
            return mid
        elif a[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def find_magic2_aux(a, left, right):
    """Not distinct values"""
    if left > right or left < 0 or right >= len(a):
        return -1
    mid = (left + right) / 2
    if a[mid] == mid:
        return mid
    # Search left part
    left_end = min(mid - 1, a[mid])
    l = find_magic2_aux(a, left, left_end)
    if l >= 0:
        return l
    right_start = max(mid + 1, a[mid])
    r = find_magic2_aux(a, right_start, right)
    return r


def find_magic2(a):
    left = 0
    right = len(a) - 1
    return find_magic2_aux(a, left, right)


def find_magic3_aux(a, left, right):
    if left > right or left < 0 or right >= len(a):
        return -1
    mid = (left + right) / 2
    if a[mid] == mid:
        return mid
    elif a[mid] < mid:
        return find_magic3_aux(a, mid + 1, right)
    else:
        return find_magic3_aux(a, left, mid - 1)


def find_magic3(a):
    """Distinct values, Recursive"""
    left = 0
    right = len(a) - 1
    return find_magic3_aux(a, left, right)


def _test():
    pass


def _print():
    a1 = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
    r1 = find_magic1(a1)
    a2 = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    r2 = find_magic2(a2)
    r3 = find_magic3(a1)
    print(r1)
    print(r2)
    print(r3)


if __name__ == '__main__':
    _test()
    _print()
