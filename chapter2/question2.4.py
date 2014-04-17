from __future__ import print_function
from linked_list import create_list, restore_list


def partition(head, x):
    """
    Maintain only one new list with two pointers (`p` and `q`)
    """
    p = q = None  # p and q point to the start and end of the new list
    while head is not None:
        next_node = head.next
        if p is None or q is None:
            q = head
            p = head
            head.next = None
        elif head.data < x:
            head.next = p
            p = head
        else:
            q.next = head
            q = q.next
            q.next = None
        head = next_node
    return p


def _test():
    pass


def _print():
    a1 = [2]
    a2 = [1, 2, 1]
    a3 = [1, 2, 3, 4, 1]
    a4 = [2, 0, 2]
    l1 = create_list(a1)
    l2 = create_list(a2)
    l3 = create_list(a3)
    l4 = create_list(a4)
    p1 = partition(l1, 2)
    p2 = partition(l2, 2)
    p3 = partition(l3, 3)
    p4 = partition(l4, 1)
    print(restore_list(p1))
    print(restore_list(p2))
    print(restore_list(p3))
    print(restore_list(p4))


if __name__ == '__main__':
    _test()
    _print()
