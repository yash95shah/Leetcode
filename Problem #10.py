# Determine if one bianry tree is actually a subtree of another binary tree]

class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def tree_generator(node):
    if not node: return
    yield node
    for child in tree_generator(node.left): yield child
    for child in tree_generator(node.right): yield child


if __name__ is '__main__':
    main()
