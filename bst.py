#! /usr/bin/python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None: self.root = Node(val)
        if val < self.root.val and self.root.left:
            self.root.left.add(val)
        elif val < self.root.val and not self.root.left:
            self.root.left = Node(val)
        if val > self.root.val and self.root.right:
            self.root.right.add(val)
        elif val > self.root.val and not self.root.right:
            self.root.right = Node(val)

    def check_if_value_exists(self, val, root):
        if not self.root: return None
        if val == self.root.val:
            return self.root
        elif val < self.root.val and self.root.left:
            self.root.left.check_if_value_exists(val)
        elif val > self.root.val and self.root.right:
            self.
