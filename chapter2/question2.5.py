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


def get_length(head):
    return len(restore_list(head))


def pad_list(head, n):
    """Pad a linked list with zeros before head"""
    for i in range(n):
        new_head = ListNode(0)
        new_head.next = head
        head = new_head
    return head


def add_lists2_aux(l1, l2, res):
    """Add two equal-size linked lists that store digits in forward order"""
    if l1 is None and l2 is None:
        return 0
    carry = add_lists2_aux(l1.next, l2.next, res)
    data = (l1.data + l2.data + carry) % 10
    carry = 1 if l1.data + l2.data + carry >= 10 else 0
    res.insert(0, data)
    return carry


def add_lists2(l1, l2):
    len1 = get_length(l1)
    len2 = get_length(l2)
    if len1 < len2:
        l1 = pad_list(l1, len2 - len1)
    else:
        l2 = pad_list(l2, len1 - len2)
    t = []
    carry = add_lists2_aux(l1, l2, t)
    res = create_list(t)
    if carry > 0:
        new_head = ListNode(1)
        new_head.next = res
        res = new_head
    return res


def add_lists3(l1, l2):
    r1 = reverse_list(l1)
    r2 = reverse_list(l2)
    res = add_lists(r1, r2)
    return reverse_list(res)


def _test():
    pass


def _print():
    a1 = [1, 2, 3, 4]
    l1 = create_list(a1)
    r1 = reverse_list(l1)
    print(restore_list(r1))
    n1 = [6, 1, 7]
    n2 = [2, 9, 5]
    nl1 = create_list(n1)
    nl2 = create_list(n2)
    r = add_lists2(nl1, nl2)
    print(restore_list(r))
    n3 = [1, 2, 3]
    n4 = [2, 3, 4]
    nl3 = create_list(n3)
    nl4 = create_list(n4)
    nl5 = create_list([9, 3, 4, 7])
    nl6 = create_list([9, 7, 2])
    rr = add_lists2(nl5, nl6)
    print(restore_list(rr))
    rrr1 = add_lists3(nl3, nl4)
    rrr2 = add_lists3(nl5, nl6)
    print(restore_list(rrr1))
    print(restore_list(rrr2))


if __name__ == '__main__':
    _test()
    _print()
