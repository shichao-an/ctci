from __future__ import print_function
from tree import create_tree


def lowest_common_ancestor_aux(root, p, q):
    """Assume both `p` and `q` exist in `root`"""
    if root is None:
        return None
    if p == root or q == root:
        return root
    left_lca = lowest_common_ancestor_aux(root.left, p, q)
    right_lca = lowest_common_ancestor_aux(root.right, p, q)
    if left_lca is None:
        return right_lca
    if right_lca is None:
        return left_lca
    return root


def exists(root, node):
    """Check whether `node` exists in root"""
    if root is None or node is None:
        return False
    if root == node:
        return True
    else:
        return exists(root.left, node) or exists(root.right, node)


def lowest_common_ancestor(root, p, q):
    if not exists(root, p) or not exists(root, q):
        return None
    return lowest_common_ancestor_aux(root, p, q)


def _test():
    pass


def _print():
    t1 = create_tree([3, 1, 5, None, None, 4, 8])
    n3 = t1
    n1 = n3.left
    n5 = n3.right
    n4 = n5.left
    n8 = n5.right
    n7 = create_tree([7])
    res1 = lowest_common_ancestor(n3, n1, n8)
    res2 = lowest_common_ancestor(n3, n4, n8)
    res3 = lowest_common_ancestor(n3, n5, n8)
    res4 = lowest_common_ancestor(n3, n5, n7)
    print(res1.data, res2.data, res3.data, res4)


if __name__ == '__main__':
    _test()
    _print()
