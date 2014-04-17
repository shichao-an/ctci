from __future__ import print_function


class SortedStack(object):
    def __init__(self):
        self.stack = []
        self.aux_stack = []

    def push(self, data):
        while self.stack and self.stack[-1] > data:
            self.aux_stack.append(self.stack.pop())
        self.stack.append(data)
        while self.aux_stack:
            self.stack.append(self.aux_stack.pop())

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


def _test():
    pass


def _print():
    s = SortedStack()
    s.push(4)
    s.push(3)
    s.push(1)
    s.push(2)
    s.push(5)
    s.push(1)
    print(s.stack)


if __name__ == '__main__':
    _test()
    _print()
