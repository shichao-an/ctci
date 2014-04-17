from __future__ import print_function


class StackMin(object):
    """Stack with min() method in O(1)"""
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def min(self):
        return self.min_stack[-1]

    def push(self, data):
        self.stack.append(data)
        if self.min_stack and data > self.min_stack[-1]:
            pass
        else:
            self.min_stack.append(data)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()


def _test():
    pass


def _print():
    stack = StackMin()
    stack.push(2)
    print(stack.min())
    stack.push(3)
    print(stack.min())
    stack.push(1)
    stack.push(5)
    stack.push(1)
    print(stack.stack)
    print(stack.min())
    stack.pop()
    print(stack.min())
    stack.pop()
    stack.pop()
    print(stack.min())


if __name__ == '__main__':
    _test()
    _print()
