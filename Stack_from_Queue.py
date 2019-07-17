import queue


class Stackedit:
    def __init__(self):
        self.q = queue.Queue(maxsize=5)
        self.s = queue.Queue(maxsize=5)

    def push(self, x):
        self.s.put(x)
        # print (self.q.empty())
        while not self.q.empty():
            y = self.q.get()
            self.s.put(y)
        temp = self.q
        self.q = self.s
        self.s = temp
        return

    def pop(self):
        return self.q.get()


'''
self.q  =   
self.s  =   4 -> 5  
'''

n = Stackedit()
n.push(4)
n.push(5)
n.push(6)
print(n.pop())
