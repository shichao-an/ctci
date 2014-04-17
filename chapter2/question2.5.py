from __future__ import print_function
from linked_list import ListNode, create_list, restore_list


def reverse_list(head):
    """Reverse a linked list"""
    prev = None
    while head is not None:
        next_node = head.next
        if prev is None:
            prev = head
            prev.next = None
        else:
            head.next = prev
            prev = head
        head = next_node
    return prev


def add_lists(l1, l2):
    """
    Two lists contain digits stored in reverse order
    """
    p = res = None
    carry = 0
    while l1 is not None or l2 is not None:
        data1 = 0
        data2 = 0
        if l1 is not None:
            data1 = l1.data
            l1 = l1.next
        if l2 is not None:
            data2 = l2.data
            l2 = l2.next
        data = (data1 + data2 + carry) % 10
        carry = 1 if data1 + data2 + carry >= 10 else 0
        if res is None:
            res = create_list([data])
            p = res
        else:
            p.next = ListNode(data)
            p = p.next
    if carry > 0:
        p.next = ListNode(1)
    return res


def _test():
    pass


def _print():
    a1 = [1, 2, 3, 4]
    l1 = create_list(a1)
    r1 = reverse_list(l1)
    print(restore_list(r1))
    n1 = [6, 1, 7]
    n2 = [2, 9]
    nl1 = create_list(n1)
    nl2 = create_list(n2)
    r = add_lists(nl1, nl2)
    print(restore_list(r))


if __name__ == '__main__':
    _test()
    _print()
