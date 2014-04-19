from __future__ import print_function
from tree import create_tree


def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1


def is_balanced(root):
    """O(n^2)"""
    if root is None:
        return True
    lb = is_balanced(root.left)
    rb = is_balanced(root.right)
    tb = abs(get_height(root.left) - get_height(root.right)) <= 1
    return lb and rb and tb


def get_height2(root):
    """Get height and check whether balanced"""
    if root is None:
        return 0
    lh = get_height2(root.left)
    rh = get_height2(root.right)
    if lh != -1 and rh != -1:
        if abs(lh - rh) <= 1:
            return max(lh, rh) + 1
    return -1


def is_balanced2(root):
    return get_height2(root) != -1


def _test():
    pass


def _print():
    a1 = [1, None, 2, 3]
    t1 = create_tree(a1)
    a2 = [1, 2, 3]
    t2 = create_tree(a2)
    print(is_balanced(t1))
    print(is_balanced(t2))


if __name__ == '__main__':
    _test()
    _print()
