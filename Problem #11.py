# Return an array of linked lists containing all elements on each depth
# of a binary tree.


def list_of_depths(binary_tree):
    pass


class treeNode():  # For the tree node only
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right
        self.depth = None

    def __str__(self):
        return "Value" + str(self.data)


class ListNode():  # For the linkedlist only
    def __init__(self, data=None, next=None):
        self.data, self.next = data, next

    def __str__(self):
        return str(self.data) + ',' + str(self.next)


class Queue():
    def __init__(self):
        self.head, self.tail = None, None

    def add(self, item):
        if self.head:  # if the head node exists
            self.tail.next = ListNode(item)
            self.tail = self.tail.next
        else:  # if this is the first element of the list
            self.head = self.tail = ListNode(item)

    def remove(self):
        if not self.head:
            return None
        item = self.head.data
        self.head = self.head.next
        return item

    def __str__(self):
        if not head:
            return "Nothing dumbass"
        item = self.head
        print(str(item))
        while item != self.tail:
            item = item.next
            print(str(item))
        return None


if __name__ is '__main__':
    queue = Queue()
    queue.add(5)
    node = ListNode(3)
    print(node)
    queue.add(node)
    queue.remove()
    print(queue)
