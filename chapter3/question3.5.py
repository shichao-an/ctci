from __future__ import print_function


class StackQueue(object):
    """Queue implemented with two stacks"""
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self):
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]


def _test():
    pass


def _print():
    q = StackQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    d1 = q.dequeue()
    print(d1)
    print(q.peek())


if __name__ == '__main__':
    _test()
    _print()
