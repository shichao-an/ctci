from __future__ import print_function
import sys
sys.path.append('..')
from chapter2.linked_list import ListNode, restore_list
from tree import create_tree


def create_level_linked_list_aux(root, lists, level):
    """Preorder recursive"""
    if root is None:
        return
    # If `lists` does not contain any node at the level
    if len(lists) == level:
        l = ListNode(root.data)
        lists.append(l)
    else:
        l = lists[level]
        l.next = ListNode(root.data)
    create_level_linked_list_aux(root.left, lists, level + 1)
    create_level_linked_list_aux(root.right, lists, level + 1)


def create_level_linked_list(root):
    res = []
    create_level_linked_list_aux(root, res, 0)
    return res


def create_level_linked_list2(root):
    """Level order"""
    res = []
    if root is None:
        return res
    queue = []
    level = ListNode(root.data)
    res.append(level)
    queue.append(root)
    queue.append(None)
    # `p` is a pointer to the last node of the linked list
    level = ListNode(0)  # Second level
    p = level
    while queue:
        root = queue.pop(0)
        if root is None:
            if level.next is not None:
                res.append(level.next)
            if queue:
                queue.append(None)
            level = ListNode(0)  # Dummy head for the next level
            p = level
        else:
            if root.left is not None:
                queue.append(root.left)
                p.next = ListNode(root.left.data)
                p = p.next
            if root.right is not None:
                queue.append(root.right)
                p.next = ListNode(root.right.data)
                p = p.next
    return res


def _test():
    pass


def _print():
    a1 = [1, 2, 3, 4, 5]
    a2 = [1, None, 3, None, 4]
    t1 = create_tree(a1)
    t2 = create_tree(a2)
    r1 = create_level_linked_list2(t1)
    r2 = create_level_linked_list2(t2)
    for l in r1:
        print(restore_list(l))
    for l in r2:
        print(restore_list(l))


if __name__ == '__main__':
    _test()
    _print()
