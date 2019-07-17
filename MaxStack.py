# max stack returns the max value of the stack
# what sort of data

# 1 -> 2 -> 3


'''

2
self.stack   2->1
self.max     1



'''


class Node():
    def __init__(self, val, next=None, oldmax=None):
        self.val, self.next, self.oldmax = val, next, oldmax


class MaxStack:
    def __init__(self):
        stack = None
        max = None

    def push(self, x):
        n = Node(x)
        if not self.stack:
            self.stack = n
        else:
            n.next = self.stack
            self.stack = n
        if not self.max or n.val > self.max.val:
            n.oldmax = self.max
            self.max = n

    def pop(self):
        if not self.stack: return
        n = stack
        self.stack = n.next
        if not n.oldMax: self.max = n.oldMax
        return n.val

    def max(self):
        if not self.max: return
        return self.max.val
