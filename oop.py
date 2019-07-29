from removeDups import Node, LinkedList


ll=LinkedList(4)
ll.append(31)
ll.append(12)
ll.append(4)
ll.append(12)
ll.append(8)
ll.append(4)
ll.printList()

ll.removeDups()
print (ll.buffer)
ll.printList()