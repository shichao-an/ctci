from __future__ import print_function


class StackSet(object):
    def __init__(self):
        self.stacks = []
        self.capacity = 3

    def push(self, data):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            stack = []
            stack.append(data)
            self.stacks.append(stack)
        else:
            self.stacks[-1].append(data)

    def pop(self):
        data = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()  # Remove the last stack
        return data

    def left_shift(self, index, top=True):
        stack = self.stacks[index]
        res = None
        if top:
            res = stack.pop()
        else:
            res = stack.pop(0)
        if not stack:  # This can only be the last stack
            self.stacks.pop()
        elif len(self.stacks) > index + 1:
            shifted = self.left_shift(index + 1, False)
            stack.append(shifted)
        return res

    def pop_at(self, index):
        return self.left_shift(index)


def _test():
    stack_set = StackSet()
    for i in range(10):
        stack_set.push(i)
    print(stack_set.stacks)
    assert stack_set.pop() == 9
    assert stack_set.pop_at(0) == 2
    assert stack_set.pop_at(1) == 6


def _print():
    pass


if __name__ == '__main__':
    _test()
    _print()
