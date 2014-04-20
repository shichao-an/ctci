"""Binary search tree"""
from tree import TreeNode


class BSTNode(TreeNode):
    def __init__(self, data):
        self.parent = None
        super(BSTNode, self).__init__(data)


def bst_search(root, data):
    if root is None:
        return None
    if data == root.data:
        return data
    elif data < root.data:
        return bst_search(root.left, data)
    else:
        return bst_search(root.right, data)


def bst_search2(root, data):
    while root is not None:
        if data == root.data:
            return data
        elif data < root.data:
            root = root.left
        else:
            root = root.right
    return None


def bst_min(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root


def bst_max(root):
    if root is None:
        return None
    while root.right is not None:
        root = root.right
    return root


def bst_insert(root, data):
    """Return the root node after insertion, since root may be None"""
    node = BSTNode(data)
    if root is None:
        return node
    current = root
    while current is not None:
        # Find the appropriate location
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right
    node.parent = parent
    if data <= parent.data:
        parent.left = node
    else:
        parent.right = node
    return root
