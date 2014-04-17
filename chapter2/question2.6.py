from __future__ import print_function
from linked_list import create_list, restore_list


def has_cycle(head):
    """Determine whether a linked list has a cycle"""
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def find_beginning(head):
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if fast is None or fast.next is None:
        return None
    slow = head
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return fast


def _test():
    pass


def _print():
    a1 = [1, 2, 3, 4, 5]
    l1 = create_list(a1)
    p = l1
    while p.next is not None:
        p = p.next
    p.next = l1.next.next
    res = find_beginning(l1)
    print(res.data)
    a2 = [1, 2]
    l2 = create_list(a2)
    l2.next.next = l2.next
    print(find_beginning(l2).data)


if __name__ == '__main__':
    _test()
    _print()
