from __future__ import print_function
from bst import bst_min, bst_max


def bst_successor(node):
    """Inorder successor of a BST node"""
    if node is None:
        return None
    if node.right is not None:
        return bst_min(node.right)
    parent = node.parent
    while parent is not None and node != parent.left:
        node = parent
        parent = parent.parent
    return parent


def bst_predecessor(node):
    if node is None:
        return None
    if node.left is not None:
        return bst_max(node.left)
    parent = node.parent
    while parent is not None and node != parent.right:
        node = parent
        parent = parent.parent
    return parent


def _test():
    pass


def _print():
    pass


if __name__ == '__main__':
    _test()
    _print()
