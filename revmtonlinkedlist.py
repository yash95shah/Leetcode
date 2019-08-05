#Reverse a linked List from position m to n
# 
# 

class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None



class LinkedList():
    def __init__(self, root):
        self.root = Node(root)

    def append(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            current = self.root
            while current.next:
                current = current.next
            current.next = Node(data)
        return

    def printList(self):
        current = self.root
        answer = ""
        while current:
            answer += str(current.val)+" --> "
            current = current.next
        answer += "None"
        print (answer)
        return

    def reverse_sub(self, m, n):
        if m > n: return
        dummy = Node(0)
        dummy.next = self.root
        #print (dummy.next.val)
        start = dummy

        for i in range(m-1):
            start = start.next
        end = cur = start.next
        prev = None

        for i in range(n-m+1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        start.next = prev
        end.next = cur

        return 
        

        

     
            



        


if __name__ is '__main__':
    root = 3
    l_list = LinkedList(3)
    l_list.append(6)
    l_list.append(5)
    l_list.append(4)
    l_list.append(8)
    l_list.printList()
    l_list.reverse_sub(2,4)
    #print ("You there")
    l_list.printList()