'''
array = [ 0 0 0 0 0 ]
After implementing push(5)
array =  [ 5 0 0 0 0 ]
push(4) -> array = [ 5 4 0 0 0 ]

iniitially push it to the closest available position.
run a while loop to actually check where exactly the push needs to happen

'''


class PriorityQueue:
    def __init__(self, maxsize):
        self).maxsize = maxSsize
        self.heap = list()
    def push(self, data):
        self.heap.append(data)
        pos = len(self.heap)
        while pos > 0:
            if self.heap[pos] < self.heap[len(self.heap)]
                self.swap_members(pos, len(self.heap))

            pos -= 1
        return

    def swap_members(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def pop(self):
