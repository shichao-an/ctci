from __future__ import print_function
from linked_list import create_list


def is_palindrome(head):
    if head is None or head.next is None:
        return True
    slow = fast = head
    stack = []
    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        fast = fast.next.next
        slow = slow.next
    if fast is not None and fast.next is None:
        slow = slow.next
    while slow is not None:
        if slow.data != stack.pop():
            return False
        slow = slow.next
    return True


def _test():
    a1 = [1]
    a2 = [1, 1]
    a3 = [1, 2]
    a4 = [1, 2, 1]
    a5 = [1, 2, 3, 1]
    a6 = [1, 3, 3, 1]
    d = locals()
    da = {
        'a1': True,
        'a2': True,
        'a3': False,
        'a4': True,
        'a5': False,
        'a6': True,
    }
    for a in d:
        l = create_list(d[a])
        assert is_palindrome(l) == da[a]


def _print():
    pass


if __name__ == '__main__':
    _test()
    _print()
