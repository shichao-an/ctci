from __future__ import print_function
import sys
from tree import create_tree

last_data = None


def is_bst(root):
    global last_data
    if root is None:
        return True
    if not is_bst(root.left):
        return False
    if last_data is not None and root.data < last_data:
        return False
    last_data = root.data
    if not is_bst(root.right):
        return False
    return True


def is_bst2_aux(root, min_data, max_data):
    if root is None:
        return True
    if root.data < min_data or root.data > max_data:
        return False
    if (not is_bst2_aux(root.left, min_data, root.data)
            or not is_bst2_aux(root.right, root.data, max_data)):
            return False
    return True


def is_bst2(root):
    max_data = sys.maxint
    min_data = -sys.maxint - 1
    return is_bst2_aux(root, min_data, max_data)


def _test():
    pass


def _print():
    a1 = [2, 1, 3]
    t1 = create_tree(a1)
    a2 = [3, 1, 2]
    t2 = create_tree(a2)
    print(is_bst(t1))
    print(is_bst(t2))
    print(is_bst2(t1))
    print(is_bst2(t2))


if __name__ == '__main__':
    _test()
    _print()
