from __future__ import print_function
from tree import create_tree


def inorder_path(root, path):
    if root is None:
        path.append('#')
        return
    inorder_path(root.left, path)
    path.append(root.data)
    inorder_path(root.right, path)


def preorder_path(root, path):
    if root is None:
        path.append('#')
        return
    path.append(root.data)
    preorder_path(root.left, path)
    preorder_path(root.right, path)


def contains_tree(t1, t2):
    """Determine whether tree `t1` contains `t2`"""
    preorder1 = []
    inorder1 = []
    preorder2 = []
    inorder2 = []
    preorder_path(t1, preorder1)
    inorder_path(t1, inorder1)
    preorder_path(t2, preorder2)
    inorder_path(t2, inorder2)
    p1 = ''.join(map(str, preorder1))
    i1 = ''.join(map(str, inorder1))
    p2 = ''.join(map(str, preorder2))
    i2 = ''.join(map(str, inorder2))
    if p2 in p1 and i2 in i1:
        return True
    return False


def match_tree(t1, t2):
    """Check whether tree `t1` and `t2` are identical"""
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.data != t2.data:
        return False
    return (match_tree(t1.left, t2.left)
            and match_tree(t1.right, t2.right))


def contains_tree2(t1, t2):
    """Traverse tree `t1` to to match `t2`'s root'"""
    if t2 is None:
        return True
    if t1 is None:
        return False
    if t1.data == t2.data:
        if match_tree(t1, t2):
            return True
    return contains_tree2(t1.left, t2) or contains_tree2(t1.right, t2)


def _test():
    a1 = [1, 2, 3, 4, 5]
    t1 = create_tree(a1)
    ppath1 = []
    ipath1 = []
    preorder_path(t1, ppath1)
    inorder_path(t1, ipath1)
    print(ppath1)
    print(ipath1)


def _print():
    t1 = create_tree([1, 2, 3, 4, 5])
    t2 = create_tree([2, 4, 5])
    t3 = create_tree([1, 2, 3])
    t4 = create_tree([1, 2, 4])
    t5 = create_tree([5])
    print(contains_tree2(t1, t2))
    print(contains_tree2(t1, t3))
    print(contains_tree2(t1, t4))
    print(contains_tree2(t1, t5))
    print(contains_tree(t1, t2))
    print(contains_tree(t1, t3))
    print(contains_tree(t1, t4))
    print(contains_tree(t1, t5))


if __name__ == '__main__':
    _test()
    _print()
