from __future__ import print_function
from linked_list import create_list, restore_list


def nth_to_last(head, k):
    """nth to last node (recursive)
    If k is greater than the length of the linked list, return head node
    """
    if head is None or k == 0:
        return None
    elif nth_to_last(head.next, k - 1) == head.next:
        return head
    else:
        return nth_to_last(head.next, k)


def nth_to_last2(head, k):
    """Use counter and print the element"""
    if head is None:
        return 0
    i = nth_to_last2(head.next, k) + 1
    if i == k:
        print(head.data)
    return i


def _test():
    pass


def _print():
    a1 = [1, 2, 3, 4, 5, 6]
    l1 = create_list(a1)
    print(nth_to_last(l1, 0))
    print(nth_to_last(l1, 1).data)
    print(nth_to_last(l1, 3).data)
    print(nth_to_last(l1, 6).data)
    print(nth_to_last(l1, 7).data)
    nth_to_last2(l1, 4)


if __name__ == '__main__':
    _test()
    _print()
