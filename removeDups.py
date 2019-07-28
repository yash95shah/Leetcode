class Node:

    def __init__(self, val):
        self.val = val
        self.next =None

class LinkedList:

    def __init__(self, head):
        self.head = Node(head)
        #self.next = None
        self.buffer = [self.head.val]
        self.allDone = False

    def append(self, data):
        if not self.head: 
            self.head = Node(data)
        else:
            currentPtr = self.head
            while (currentPtr.next):
                currentPtr = currentPtr.next
            currentPtr.next = Node(data)
        return 

    def removeDups(self):
        prev = self.head
        curr = self.head.next
        
        while (curr ):
            if curr.val in self.buffer:
                #print (curr.next.val)
                prev.next = curr.next
                curr = curr.next
               # self.removeDups()
            else:
                # print (curr.val)
                self.buffer.append(curr.val)
                prev = prev.next
                curr = curr.next
             
            

        return

    def printList(self):
        o_str=""
        curr = self.head
        while curr:
            o_str += str(curr.val)+"-->"
            curr=curr.next
        o_str += "None"
        print(o_str)
        return 





    

ll=LinkedList(4)
ll.append(11)
ll.append(11)
ll.append(4)
ll.append(4)
ll.append(8)
ll.append(4)
ll.printList()

ll.removeDups()
print (ll.buffer)
ll.printList()