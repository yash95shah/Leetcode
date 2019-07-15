# Proprietary Code requested by Catherine Luse.
# Copying or implementation of this code in any way, shape or form is liable to a legal citation.

class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next


class LinkedList:
    def __init__(self, root):
        self.root = Node(root)

    def appendItem(self, x):
        ex = Node(x, None)
        if not self.root: root = ex
        current = self.root
        while current.next:
            current = current.next
        current.next = ex
        return self.root

    def __str__(self):
        current = self.root
        mayo = str()
        while current.next:
            mayo += str(current.val) + '->'
            current = current.next
        mayo += 'None'
        return mayo


class Solution:
    def __init__(self):
        pass

    def sortList(self, head):
        if not head or not head.next: return head
        l1, l2 = self.splitList(head=head)
        l1 = self.sortList(head=l1)
        l2 = self.sortList(head=l2)
        head = self.mergelists(l1, l2)
        return head

    def splitList(self, head):
        fast_ptr, slow_ptr = head, head
        if fast_ptr:
            fast_ptr = fast_ptr.next
        while fast_ptr:
            fast_ptr = fast_ptr.next
            if fast_ptr:
                fast_ptr = fast_ptr.next
                slow_ptr = slow_ptr.next
            mid = slow_ptr.next
            return head, mid

    def mergeLists(self, list1_head, list2_head):
        if not list1_head: return list2_head
        if not list2_head: return list1_head
        if list1_head.val <= list2_head.val:
            temp = list1_head
            temp.next = self.mergeLists(list1_head=list1_head.next, list2_head=list2_head)
        else:
            temp = list2_head
            temp.next = self.mergeLists(list1_head=list1_head, list2_head=list2_head.next)
        return temp


if __name__ is '__main__':
    newLL = LinkedList(5)
    newLL.appendItem(3)
    newLL.appendItem(13)
    newLL.appendItem(54)
    newLL.appendItem(23)
    newLL.appendItem(51)
    newLL.appendItem(75)
    newLL.appendItem(17)
    str(newLL)
    newsol = Solution()
    newsol.sortList(newLL.root)
    print(newLL)
