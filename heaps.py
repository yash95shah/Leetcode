'''
heapq
------
Methods

heapify: - Converts a regular list into a heap. The smallest element gets pushed to the 0th index.

heappush: - Adds an element to the heap without altering the heap.

heappop: - returns the smallest element from the heap

heapreplace: - It replaces the smallest element with the newly supplied value






'''

import heapq

H = [3, 5, 4, 1, 2, 6, 7, 8, 9, 12]
heapq.heapify(H)
print(H)
heapq.heappush(H, 0)
heapq.heapreplace(H, 102)
print(H)
heapq.heappop(H)
print(H)
