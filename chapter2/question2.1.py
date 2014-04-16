from __future__ import print_function
from linked_list import create_list, restore_list


def delete_duplicates(head):
    t = {}
    prev = None
    while head is not None:
        next_node = head.next
        if head.data in t:
            prev.next = next_node
            # free(head) as in C
        else:
            t[head.data] = True
            prev = head
        head = next_node


def delete_duplicates2(head):
    """No buffer"""
    if head is None:
        return
    while head is not None:
        p = head.next
        prev = head
        while p is not None:
            next_node = p.next
            if p.data == head.data:
                prev.next = next_node
                # free(p) as in C
            else:
                prev = p
            p = next_node
        head = head.next


def _test():
    pass


def _print():
    a1 = [1, 2, 1, 3, 1, 2, 4, 5]
    l1 = create_list(a1)
    delete_duplicates2(l1)
    a2 = [1, 1, 1]
    l2 = create_list(a2)
    delete_duplicates2(l2)
    print(restore_list(l1))
    print(restore_list(l2))


if __name__ == '__main__':
    _test()
    _print()
