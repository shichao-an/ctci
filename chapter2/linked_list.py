"""Linked List library for Chapter 2"""
from __future__ import print_function


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def create_list(a):
    """Create a singly linked list from an array `a`"""
    if not a:
        return None
    q = p = ListNode(a[0])
    for i in range(1, len(a)):
        p.next = ListNode(a[i])
        p = p.next
    return q


def restore_list(p):
    """Return array (Python list) from a linked list"""
    res = []
    while p is not None:
        res.append(p.data)
        p = p.next
    return res
