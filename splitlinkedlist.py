class LinkedList:
    def __init__(self, root):
        self.root = Node(root)

    def append(self, x):
        x_node = Node(x)
        if not self.root: x_node = self.root
        temp = root
        while temp.next:
            temp = temp.next
        temp.next = x_node

    def spitlist(self):
        pointer1, pointer2 = self.root, self.root
        if pointer1:
            pointer1 = pointer1.next
        while pointer1:
            if pointer1:
                pointer1 = pointer1.next
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        mid = pointer2.next
        pointer2.next = None
        return self.root, mid


class Node:
    def __init__(self, val, next):
        self.val, self.next = val, next
