from __future__ import print_function
from tree import TreeNode


def create_min_bst_aux(a, l, r):
    if not a:
        return None
    if l > r:
        return None
    mid = l + (r - l) // 2
    root = TreeNode(a[mid])
    root.left = create_min_bst_aux(a, l, mid - 1)
    root.right = create_min_bst_aux(a, mid + 1, r)
    return root


def create_min_bst(a):
    return create_min_bst_aux(a, 0, len(a) - 1)


def _test():
    pass


def _print():
    a0 = [1]
    a1 = [1, 2]
    a2 = [1, 2, 3]
    a3 = [1, 2, 3, 4]
    t0 = create_min_bst(a0)
    t1 = create_min_bst(a1)
    t2 = create_min_bst(a2)
    t3 = create_min_bst(a3)


if __name__ == '__main__':
    _test()
    _print()
