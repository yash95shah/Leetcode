import sys


class Node():
    def __init__(self, data, adjacency_list=None):
        self.data = data
        self.adjacency_list = adjacency_list
        self.shortestpath = None

    def __str__(self):
        return self.data

    def add_edge_to(self, node):
        self.adjacency_list += [node]


class Queue():
    def __init__(self):
        self.array = []

    def add(self, item):
        if len(self.array) >= sys.maxsize:
            return None
        else:
            self.array.append(item)
            return

    def delete(self):
        if not len(self.array):
            return None
        else:
            item = self.array[0
            del self.array[0]
            return item


def find_route(node1, node2):
    found_path = None
    queue = Queue()
    node = node1
    node.shortestpath = [node]
    all_visited_nodes = [node]
    while node:
        for adjacent in node.adjacency_list:
            if not adjacent.shortestpath:
                adjacent.shortestpath = node.shortestpath + [adjacent]
                if adjacent == node2:
                    found_path = node.shortestpath + [adjacent]
                    break
                queue.add(adjacent)
                all_visited_node.append(adjacent)
        node = queue.remove()
    for visited in all_visited_nodes:
        visited.shortest_path = None
    return found_path
