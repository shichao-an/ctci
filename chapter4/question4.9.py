from __future__ import print_function
from tree import create_tree


def find_sum_aux(root, s, path):
    if root is None:
        return
    path.append(root.data)
    i = len(path) - 1
    t = 0
    while i >= 0:
        t += path[i]
        if t == s:
            print_path(path, i)
        i -= 1
    find_sum_aux(root.left, s, path)
    find_sum_aux(root.right, s, path)
    path.pop()


def find_sum(root, s):
    path = []
    return find_sum_aux(root, s, path)


def print_path(path, i):
    """Print path from index `i` up"""
    print(path[i:])


def _test():
    pass


def _print():
    a1 = [1, 2, 3, 4, 5, None, None, -1]
    t1 = create_tree(a1)
    find_sum(t1, 3)


if __name__ == '__main__':
    _test()
    _print()
