from __future__ import print_function
from linked_list import create_list, restore_list


def delete_node(node):
    """
    Delete a node in the middle of a singly linked list
    """
    if node is None or node.next is None:
        return
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next


def _test():
    pass


def _print():
    a1 = [1, 2, 3, 4, 5]
    l1 = create_list(a1)
    node = l1.next.next  # 3
    delete_node(node)
    print(restore_list(l1))


if __name__ == '__main__':
    _test()
    _print()
