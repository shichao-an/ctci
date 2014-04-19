from __future__ import print_function


class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree(a):
    """
    Create a binary tree from array `a` with notation like
    [1, None, 2, 3]
       1
        \
         2
        /
       3
    """
    queue = []
    if not a:
        return None
    root_data = a.pop(0)
    root = TreeNode(root_data)
    queue.append(root)
    while queue:
        node = queue.pop(0)
        left_data = a.pop(0) if a else None  # Pop if `a` is not empty
        right_data = a.pop(0) if a else None
        if left_data is not None:
            left = TreeNode(left_data)
            node.left = left
            queue.append(left)
        if right_data is not None:
            right = TreeNode(right_data)
            node.right = right
            queue.append(right)
    return root
